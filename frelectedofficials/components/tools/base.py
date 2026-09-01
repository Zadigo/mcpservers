from fastmcp.prompts import Message
from fastmcp.tools import tool
from mcp.types import PromptMessage

from models.base import FileInfo, get_registry


@tool
def list_datasets() -> list[FileInfo]:
    """List all the datasets in the registry."""
    return get_registry ().files


@tool
def get_dataset(name: str) -> FileInfo | None:
    """Get a dataset by name.
    
    Args:
        name (str): The name of the dataset to retrieve.
    """
    result = get_registry().get_file_by_title(name)

    if result is None:
        return PromptMessage(
            messages=[
                Message()
            ]
        )

    return result
@tool
def get_elected_official_in_dataset(name: str, dataset_name: str) -> dict:
    pass
