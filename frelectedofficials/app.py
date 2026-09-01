# import asyncio
from contextlib import asynccontextmanager

from fastmcp import FastMCP
from fastmcp.server.providers import FileSystemProvider
from fastmcp.server.providers.skills import SkillsDirectoryProvider

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

    yield


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
