from contextlib import asynccontextmanager

from fastmcp import FastMCP
from fastmcp.resources import DirectoryResource

# from fastmcp.server.auth.providers.github import GitHubProvider
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

from models.base import BusinessColumnEnum

# from ui.university import ui_app
from utils import BASE_DIR, logger

# auth = GitHubProvider(
#     client_id=os.environ["GITHUB_CLIENT_ID"],
#     client_secret=os.environ["GITHUB_CLIENT_SECRET"],
#     base_url="https://your-server.com",
#     jwt_signing_key=os.environ["JWT_SIGNING_KEY"],
#     client_storage=RedisStore(host="redis.example.com", port=6379)
# )

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
        FileSystemProvider(BASE_DIR.joinpath('components'), reload=True)
    ]
)

mcp.add_provider(SkillsDirectoryProvider(roots=BASE_DIR.joinpath(".claude", "skills")))


if BASE_DIR.joinpath('components', 'resources', 'data').is_dir():
    fullpath = BASE_DIR.joinpath('components', 'resources', 'data')

    static_resources = DirectoryResource(
        uri=AnyUrl("resource://dataset-descriptions"),
        path=fullpath,
        name="Dataset Descriptions",
        description="Contains descriptions of various datasets available for analysis.",
        recursive=False
    )

    mcp.add_resource(static_resources)


@mcp.completion
async def completion(ref: PromptReference | ResourceTemplateReference, argument: CompletionArgument, context: CompletionContext | None = None):
    column_names = list(BusinessColumnEnum.__members__)
    
    if isinstance(ref, PromptReference):
        tool_names = ['explain_column', 'legal_units_exact_search', 'legal_units_column_has_no_value']

        if ref.name in tool_names and argument.name == 'column_name':
            return sorted(column_names)

    return []
