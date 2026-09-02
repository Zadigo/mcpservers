import json

from fastmcp.prompts import Message
from fastmcp.tools import ToolResult, tool
from mcp.types import PromptMessage

from models.base import FileInfo, GroupingByGender, get_registry
from models.results import DistrictCouncillorEN


@tool
def list_datasets() -> list[FileInfo]:
    """List all the datasets in the registry."""
    return get_registry ().files


@tool
def get_dataset(name: str) -> DistrictCouncillorEN | None:
    """Get a dataset by name.
    
    Args:
        name (str): The name of the dataset to retrieve.
    Returns:
        DistrictCouncillorEN | ToolResult: The dataset model or an error message if not found.
    """
    result = get_registry().get_file_by_title(name)

    if result is None:
        return ToolResult(
            content=f"Dataset '{name}' not found. Available datasets: {get_registry().str_filetitles}",
            structured_content={'result': DistrictCouncillorEN()}
        )

    return result.get_content_as_model(DistrictCouncillorEN)


@tool
def get_elected_official_in_dataset(lastname: str, dataset_name: str, firstname: str | None = None) -> dict:
    pass


@tool
def distribution_by_gender(name: str) -> GroupingByGender:
    """Get the distribution of elected officials 
    by gender in a dataset
    
    Args:
        name (str): The name of the dataset to analyze.
    """
    registry = get_registry()
    dataset = registry.get_file_by_title(name)
    if dataset is None:
        return PromptMessage(
            messages=[
                Message(role='assistant', content=f"Dataset '{name}' not found."),
                Message(role='assistant', content=f"Available datasets: {registry.str_filetitles}")
            ]
        )
    df = dataset.get_content()
    str_data = df['code_sexe'].groupby(df['code_sexe']).count().to_json()
    return GroupingByGender(**json.loads(str_data))


