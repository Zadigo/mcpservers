from fastmcp.tools import tool
from fastmcp.tools.base import ToolResult

from components.utils import dataframe_to_models
from models.results import AssociationModel
from utils import FilesQueryset


@tool
async def search_dataset() -> list[AssociationModel]:
    """
    Search for a dataset in the database.
    """
    instance = FilesQueryset()
    df = await instance.prefetch_files()

    return ToolResult(
        content=dataframe_to_models(df)
    )
