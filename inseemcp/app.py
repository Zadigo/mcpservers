from contextlib import asynccontextmanager

from fastmcp import FastMCP
from fastmcp.apps.file_upload import FileUpload
from fastmcp.resources import DirectoryResource
from fastmcp.server.auth import JWTVerifier, MultiAuth, OAuthProxy
from fastmcp.server.middleware.caching import ResponseCachingMiddleware
from fastmcp.server.providers import FileSystemProvider, SkillsDirectoryProvider
from key_value.aio.stores.redis import RedisStore
from mcp_types import (
    CompletionArgument,
    CompletionContext,
    PromptReference,
    ResourceTemplateReference,
)
from pydantic import AnyUrl

from components.resources.constants import build_resources
from models.base import BusinessColumnEnum
from utils import BASE_DIR, logger

upstream_verifier = JWTVerifier(
    jwks_uri="https://login.example.com/.well-known/jwks.json",
    issuer="https://login.example.com",
    audience="my-app",
)

auth = MultiAuth(
    server=OAuthProxy(
        upstream_authorization_endpoint="https://login.example.com/oauth/authorize",
        upstream_token_endpoint="https://login.example.com/oauth/token",
        upstream_client_id="my-app",
        upstream_client_secret="secret",
        token_verifier=upstream_verifier,
        base_url="https://my-server.com",
    ),
    verifiers=[
        JWTVerifier(
            jwks_uri="https://internal-issuer.example.com/.well-known/jwks.json",
            issuer="https://internal-issuer.example.com",
            audience="my-mcp-server",
        ),
    ]
)

middleware = ResponseCachingMiddleware(
    cache_storage=RedisStore(host="localhost", port=6379)
)


INSTRUCTIONS: str = """
You are business analyst assistant specializing in French business data. You have access to the INSEE database 
and can provide insights, analysis, and summaries based on the data available. Your responses should be clear, 
concise, and tailored to the needs of business analysts seeking information from the INSEE database.
"""

@asynccontextmanager
async def lifespan(app: FastMCP):
    try:
        yield
    except Exception:
        logger.critical('An error occurred during the lifespan of the MCP server.', exc_info=True)
    finally:
        pass


mcp = FastMCP(
    name='FR INSEE Business Analyst Assistant',
    instructions=INSTRUCTIONS,
    lifespan=lifespan,
    on_duplicate='ignore',
    strict_input_validation=False,
    providers=[
        # ui_app,
        FileSystemProvider(BASE_DIR.joinpath('components'), reload=True),
        SkillsDirectoryProvider(roots=BASE_DIR.joinpath(".claude", "skills")),
        FileUpload(title='Enrich Dataset', description='Upload files to enrich the dataset with INSEE data.')
    ]
)


# File catalog

static_dir = BASE_DIR.joinpath('components', 'resources', 'static')
if static_dir.is_dir():
    static_resources = DirectoryResource(
        uri=AnyUrl("concepts://dataset/files"),
        path=static_dir,
        name="Dataset Documentation Files",
        description="Lists the documentation files available in the dataset resources directory.",
        recursive=True
    )

    mcp.add_resource(static_resources)


# Build and add all predefined resources to the MCP application.
build_resources(mcp)


@mcp.completion
async def completion(ref: PromptReference | ResourceTemplateReference, argument: CompletionArgument, context: CompletionContext | None = None):
    column_names = list(BusinessColumnEnum.__members__)
    
    if isinstance(ref, PromptReference):
        tool_names = ['explain_column', 'legal_units_exact_search', 'legal_units_column_has_no_value']

        if ref.name in tool_names and argument.name == 'column_name':
            return sorted(column_names)

    return []
