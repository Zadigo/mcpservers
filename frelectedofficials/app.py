# import asyncio
from contextlib import asynccontextmanager

from fastmcp.server import FastMCP
from fastmcp.server.providers import FileSystemProvider
from fastmcp.server.providers.skills import SkillsDirectoryProvider
from mcp.types import (
    CompletionContext,
    PromptArgument,
    PromptReference,
    ResourceTemplateReference,
)

from models.base import get_registry
from utils import BASE_DIR

# from endpoints import (
#     AbstractCreator,
#     ConcreteDistrictCouncillor,
#     generate_elected_officials,
# )


@asynccontextmanager
async def lifespan(app: FastMCP):
    # officials: AbstractCreator = [
    #     ConcreteDistrictCouncillor()
    # ]

    # tasks = [asyncio.create_task(generate_elected_officials(official)) for official in officials]
    # semaphore = asyncio.Semaphore(2)
    # async with semaphore:
    #     await asyncio.gather(*tasks)
    try:
        yield
    finally:
        pass


app = FastMCP(
    name="French Elected Officials",
    instructions='This is an MCP server for adding context to an LLM about French elected officials.',
    lifespan=lifespan,
    on_duplicate='ignore',
    providers=[
        FileSystemProvider(BASE_DIR.joinpath('components'), reload=True)
    ]
)

app.add_provider(SkillsDirectoryProvider(roots=BASE_DIR.joinpath(".claude", "skills")))



@app.completion
def complete(ref: PromptReference, argument: PromptArgument, context: CompletionContext):
    def run_filter():
        return [value for value in registry.filetitles if argument.value.lower() in value.lower()]

    registry = get_registry()
    if isinstance(ref, PromptReference) and ref.name == "ask_about_single_dataset" and argument.name == "name":
        return run_filter()

    if isinstance(ref, ResourceTemplateReference) and ref.name == "ask_about_single_dataset" and argument.name == "name":
        return run_filter()

    if isinstance(ref, PromptReference) and ref.name == "ask_about_dataset" and argument.name == "name":
        return run_filter()

    prompts = ['distribution_by_gender', 'get_dataset']
    if argument.name == 'name':
        return run_filter()
            
    return None
