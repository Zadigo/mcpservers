from collections.abc import Sequence
from typing import Any

import pandas
from fastmcp.tools import tool

from backend.base import UniversityRequest
from models.university import UniversityModel


def filter_data(data: Sequence[dict[str, Any]], name: str | None = None):
    df = pandas.DataFrame(data)

    if name is not None:
        df = df[
            (df["nom_court"].str.casefold() == name.casefold()) |
            (df["nom_court"].str.casefold().str.contains(name.casefold()))
        ]

    int_cols = {f"inscrits_{year}": "float" for year in range(2010, 2025)}
    dtypes = {col: int_cols.get(col, "str") for col in df.columns}
    df = df.astype(dtypes, errors='ignore')
    
    # Replace any 'nan' string values with None. The 'nan'
    # appear in pandas.DataFrame for None which are converted 
    # to the string 'nan' and breaks the model.
    # df = df.where(df.notna(), None)
    df.replace({pandas.NA: None}, inplace=True)
    df.replace({float('nan'): None}, inplace=True)
    return df.to_dict(orient="records")


@tool
async def get_university_by_name(name: str) -> list[UniversityModel]:
    instance = UniversityRequest()
    await instance()
    if instance._cached_response is None:
        return []
    data = filter_data(instance._cached_response.json(), name=name)
    return [UniversityModel(**item) for item in data]


async def get_university_by_siren(siren: str) -> list[UniversityModel]:
    instance = UniversityRequest()
    await instance()
    if instance._cached_response is None:
        return []
    data = filter_data(instance._cached_response.json(), name=None)
    data = [item for item in data if siren in item.get("siren", [])]
    return [UniversityModel(**item) for item in data]


async def get_university_by_siret(siret: str) -> list[UniversityModel]:
    instance = UniversityRequest()
    await instance()
    if instance._cached_response is None:
        return []
    data = filter_data(instance._cached_response.json(), name=None)
    data = [item for item in data if siret in item.get("siret", [])]
    return [UniversityModel(**item) for item in data]
