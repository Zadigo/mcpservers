import itertools
from contextlib import asynccontextmanager

from fastmcp import FastMCP
from fastmcp.resources import DirectoryResource
from fastmcp.server.providers import FileSystemProvider, SkillsDirectoryProvider
from mcp_types import (
    CompletionContext,
    PromptArgument,
    PromptReference,
    ResourceTemplateReference,
)

from models.base import EstablishmentEnum, LegalUnitEnum
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


if BASE_DIR.joinpath('resources', 'data').is_dir():
    fullpath = BASE_DIR.joinpath('resources', 'data')

    static_resources = DirectoryResource(
        uri="resource://dataset-descriptions",
        path=fullpath,
        name="Dataset Descriptions",
        description="Contains descriptions of various datasets available for analysis.",
        recursive=False
    )

    mcp.add_resource(static_resources)


@mcp.completion
async def complet(ref: PromptReference | ResourceTemplateReference, argument: PromptArgument, context: CompletionContext):
    if isinstance(ref, PromptReference):
        if ref.name == 'explain_column' and argument.name == 'column_name':
            column_names = itertools.chain(
                {item for item in LegalUnitEnum.__members__},
                {item for item in EstablishmentEnum.__members__}
            )
            return sorted(column_names)

        if argument.name == 'test':
            pass

    return None
