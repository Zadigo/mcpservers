from contextlib import asynccontextmanager

from fastmcp import FastMCP
from fastmcp.server.providers import FileSystemProvider, SkillsDirectoryProvider
from mcp_types import CompletionContext, PromptArgument, PromptReference

from utils import BASE_DIR, logger

INSTRUCTIONS: str = """
You are business analyst assistant specializing in French associations. Your goal is to provide
helpful business insights and analysis based on the datasets provided by the Répertoire National des Associations.
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
    name='FR Association',
    instructions=INSTRUCTIONS,
    lifespan=lifespan,
    providers=[
        FileSystemProvider(BASE_DIR.joinpath('components'), reload=True)
    ]
)

mcp.add_provider(SkillsDirectoryProvider(roots=BASE_DIR.joinpath(".claude", "skills")))

@mcp.completion
async def global_completion(ref: PromptReference, arguments: PromptArgument, context: CompletionContext):
    pass
