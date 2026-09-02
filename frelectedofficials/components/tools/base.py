
import json

from fastmcp.tools import ToolResult, tool

from models.base import FileInfo, GroupingByGender, GroupingByJobCategory, get_registry
from models.results import DistrictCouncillorEN


@tool
def list_datasets() -> list[FileInfo]:
    """List all the datasets in the registry."""
    return get_registry ().files


@tool
def get_dataset(name: str) -> list[DistrictCouncillorEN] | ToolResult:
    """Get a dataset by name.
    
    Args:
        name (str): The name of the dataset to retrieve.

    Returns:
        list[DistrictCouncillorEN] | ToolResult: The dataset model or an error message if not found.
    """
    if name == "Élus Conseiller d'Arrondissement":
        return get_district_councilor_dataset()

    return ToolResult(
        content=f"Dataset '{name}' not found. Available datasets: {get_registry().str_filetitles}",
        structured_content={'result': []},
        is_error=True
    )


@tool
def get_district_councilor_dataset() -> list[DistrictCouncillorEN] | ToolResult:
    """Get the dataset of district councilors.
    
    Returns:
        list[DistrictCouncillorEN] | ToolResult: A list of district councilor models or an error message if not found.
    """
    name = "Élus Conseiller d'Arrondissement"
    result = get_registry().get_file_by_title(name)

    if result is None:
        return ToolResult(
            content=f"Dataset '{name}' not found. Available datasets: {get_registry().str_filetitles}",
            structured_content={'result': []}
        )

    return [
        DistrictCouncillorEN(**row) 
            for row in result.get_content(as_json=True)
    ]


@tool
def get_elected_official_in_dataset(lastname: str, dataset_name: str, firstname: str | None = None) -> dict:
    """Retrieve an elected official's information from a specific dataset by their last name and optionally first name.

    Args:
        lastname (str): The last name of the elected official.
        dataset_name (str): The name of the dataset to search in.
        firstname (str | None): The first name of the elected official (optional).

    Returns:
        dict | ToolResult: The elected official's information or an error message if not found.
    """
    registry = get_registry()
    dataset = registry.get_file_by_title(dataset_name)
    if dataset is None:
        return ToolResult(
            content=f"Dataset '{dataset_name}' not found. Available datasets: {registry.str_filetitles}",
            structured_content={'result': {}},
            is_error=True
        )

    df = dataset.get_content()
    filtered = df[df['lastname'] == lastname]
    if firstname is not None:
        filtered = filtered[filtered['firstname'] == firstname]

    if filtered.empty:
        return ToolResult(
            content=f"Elected official '{lastname} {firstname or ''}' not found in dataset '{dataset_name}'.",
            structured_content={'result': {}},
            is_error=True
        )

    return filtered.to_dict(orient='records')[0]


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
        return ToolResult(
            content=f"Dataset '{name}' not found. Available datasets: {registry.str_filetitles}",
            structured_content={'result': GroupingByGender()},
            is_error=True
        )
    
    df = dataset.get_content()
    count = df['gender_code'].groupby(df['gender_code']).count()
    json_data = json.loads(count.to_json())

    return GroupingByGender(
        F=json_data.get('F', 0), 
        H=json_data.get('M', 0)
    )


@tool
def distribution_by_job_category(name: str) -> list[GroupingByJobCategory]:
    """Get the distribution of elected officials by their initial 
    job category in a dataset.
    
    Args:
        name (str): The name of the dataset to analyze.
    """
    registry = get_registry()
    dataset = registry.get_file_by_title(name)
    if dataset is None:
        return ToolResult(
            content=f"Dataset '{name}' not found. Available datasets: {registry.str_filetitles}",
            structured_content={'result': []},
            is_error=True
        )
    
    df = dataset.get_content()
    count = df['socio_professional_category_name'].groupby(df['socio_professional_category_name']).count()
    json_data = json.loads(count.to_json())

    return [
        GroupingByJobCategory(job_name=key, count=value)
        for key, value in json_data.items()
    ]
