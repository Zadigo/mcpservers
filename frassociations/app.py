from contextlib import asynccontextmanager

from fastmcp import FastMCP


@asynccontextmanager
def lifespan(app):
    try:
        yield
    except:
        pass


app = FastMCP(
    title='FR Association',
    instructions='',
    lifespan=lifespan
)
