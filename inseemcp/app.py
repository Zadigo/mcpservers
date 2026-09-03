from contextlib import asynccontextmanager

from fastmcp import FastMCP
from fastmcp.server.providers import FileSystemProvider, SkillsDirectoryProvider
from mcp_types import CompletionContext, PromptArgument, PromptReference

from utils import BASE_DIR, logger

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
    providers=[
        FileSystemProvider(BASE_DIR.joinpath('components'), reload=True)
    ]
)

mcp.add_provider(SkillsDirectoryProvider(roots=BASE_DIR.joinpath(".claude", "skills")))

@mcp.completion
async def global_completion(ref: PromptReference, arguments: PromptArgument, context: CompletionContext):
    pass
