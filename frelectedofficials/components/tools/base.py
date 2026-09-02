
import json
from typing import Literal

from fastmcp.tools import ToolResult, tool

from models.base import FileInfo, GroupingByGender, GroupingByJobCategory, get_registry
from models.results import DistrictCouncillorEN
from utils import df_to_json


@tool
def list_datasets() -> list[FileInfo]:
    """List all the datasets in the registry."""
    return get_registry ().files


@tool
def get_dataset(name: str) -> list[DistrictCouncillorEN] | ToolResult:
    """Get a dataset by name.
    
    Args:
        name (str): The name of the dataset to retrieve.
    """
    if name == "Élus Conseiller d'Arrondissement":
        return get_district_councilor_dataset()

    return ToolResult(
        content=f"Dataset '{name}' not found. Available datasets: {get_registry().str_filetitles}",
        structured_content={'result': []},
        is_error=True
    )


@tool
def get_average_age(name: str, by_gender: Literal['M', 'F'] | None  = None) -> float | ToolResult:
    """Get the average age of elected officials in a dataset.
    
    Args:
        name (str): The name of the dataset to analyze.
    """
    registry = get_registry()
    dataset = registry.get_file_by_title(name)
    if dataset is None:
        return ToolResult(
            content=f"Dataset '{name}' not found. Available datasets: {registry.str_filetitles}",
            structured_content={'result': 0},
            is_error=True
        )
    
    df = dataset.get_content()
    return df[~df['age'].isna()]['age'].mean()


@tool
def get_district_councilor_dataset() -> list[DistrictCouncillorEN] | ToolResult:
    """Get the dataset of district councilors.    
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
            for row in result.get_content_as_json()
    ]


@tool
def search_elected_official_in_dataset(dataset_name: str, lastname: str | None, firstname: str | None = None) -> list[DistrictCouncillorEN]:
    """Retrieve an elected official's information from a specific dataset by their last name and optionally first name.

    Args:
        dataset_name (str): The name of the dataset to search in.
        lastname (str | None): The last name of the elected official.
        firstname (str | None): The first name of the elected official (optional).
    """
    registry = get_registry()
    fileinfo = registry.get_file_by_title(dataset_name)
    if fileinfo is None:
        return ToolResult(
            content=f"Dataset '{dataset_name}' not found. Available datasets: {registry.str_filetitles}",
            structured_content={'result': {}},
            is_error=True
        )

    df = fileinfo.get_content()

    df['_firstname'] = False
    df['_lastname'] = False

    for item in df.itertuples():
        if firstname is not None:
            str_firstname = df.loc[item.Index, 'first_name']

            if firstname in str_firstname:
                df.loc[item.Index, '_firstname'] = True

        if lastname is not None:
            str_lastname = df.loc[item.Index, 'last_name']
            
            if lastname in str_lastname:
                df.loc[item.Index, '_lastname'] = True

    if firstname is not None and lastname is not None:
        df = df[(df['_firstname'] == True) & (df['_lastname'] == True)]
    elif firstname is not None:
        df = df[df['_firstname'] == True]
    elif lastname is not None:
        df = df[df['_lastname'] == True]

    return [DistrictCouncillorEN(**item) for item in df_to_json(df)]


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
