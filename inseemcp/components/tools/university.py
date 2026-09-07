
from typing import Any

import pandas
from fastmcp.tools import tool

from backend.base import UniversityRequest
from backend.utils import BaseRequest
from models.university import UniversityModel


def filter_data(request: BaseRequest, name: str | None = None, siren: str | None = None, siret: str | None = None) -> list[dict[str, Any]]:
    df = request.dataframe
    if name is not None:
        df = df[
            (df["nom_court"].str.casefold() == name.casefold()) |
            (df["nom_court"].str.casefold().str.contains(name.casefold()))
        ]
    
    if siren is not None:
        df = df[df["siren"].str.contains(siren)]

    if siret is not None:
        df = df[df["siret"].str.contains(siret)]

    int_cols = {f"inscrits_{year}": "float" for year in range(2010, 2025)}
    dtypes = {col: int_cols.get(col, "str") for col in df.columns}
    df = df.astype(dtypes, errors='ignore')
    
    # Replace any 'nan' string values with None. The 'nan'
    # appear in pandas.DataFrame for None which are converted 
    # to the string 'nan' and breaks the model.
    # df = df.where(df.notna(), None)
    df.replace({pandas.NA: None}, inplace=True)
    df.replace({float('nan'): None}, inplace=True)
    return df.to_dict(orient="records") # pyright: ignore[reportReturnType]


@tool
async def get_university_by_siren(siren: str) -> list[UniversityModel]:
    """Returns a university by SIREN by querying the database called
    'Principaux établissements d'enseignement supérieur' provided by the
    French Ministry of Higher Education (Ministère de l'Enseignement supérieur, 
    de la Recherche et de l'Innovation).
    
    A SIREN is a unique 9-digit identifier assigned to a legal unit
    (enterprise/company). It is different from a SIRET, which identifies
    an individual establishment belonging to that legal unit.

    When to use this tool:
    - When an initial results for a SIREN in the INSEE database points to the type of
        of establishment or legal unit being a university or a "grande école" by checking
        the NAF code for establishments that are classified as those for teaching and research: 85
        (for example 85.42Z for higher education establishments)
    - When additional context to these main results are needed by enriching them
        with data from this dataset

    Do not use this when:
    - When the user provides a SIRET instead of a SIREN
    - When the user is not looking for additional context for an 
        establishment (results provided by get_siret or get_siren)

    Example of a good use case
        1. User: "Can you find the business or university with SIREN 197517170?"
        2. Assistant: "Here are the details for the university with SIREN 197517170."
        3. User: "What more can you tell me about this business?"
        4. Assistant: [Provides additional context by querying this tool for example, using the SIREN 197517170]
    
    Args:
    siren: The 9-digit SIREN number identifying the legal unit to
        retrieve. The value should contain exactly 9 digits.

    Returns:
        A list of UniversityModel instances matching the provided SIREN.
    """
    instance = UniversityRequest()
    await instance()
    if instance._cached_response is None:
        return []
    data = filter_data(instance, siren=siren)
    return [UniversityModel(**item) for item in data]


@tool
async def get_university_by_siret(siret: str) -> list[UniversityModel]:
    """Returns a university by SIRET by querying the database called
    'Principaux établissements d\'enseignement supérieur' provided by the
    French Ministry of Higher Education (Ministère de l'Enseignement supérieur, 
    de la Recherche et de l'Innovation).
    
    A SIRET is a unique 14-digit identifier assigned to an individual establishment
    belonging to a legal unit (enterprise/company). It is different from a SIREN, 
    which identifies the legal unit itself.

    When to use this tool:
    - When an initial results for a SIRET in the INSEE database points to the type of
        of the legal unit being a university or a "grande école" by checking
        the NAF code for establishments that are classified as those for teaching and research: 85
        (for example 85.42Z for higher education establishments)
    - When additional context to these main results are needed by enriching them
        with data from this dataset

    Do not use this when:
    - When the user provides a SIREN instead of a SIRET
    - When the user is not looking for additional context for an 
        establishment (results provided by get_siret or get_siren)

    Example of a good use case
        1. User: "Can you find the business or university with SIRET 19751717000013?"
        2. Assistant: "Here are the details for the university with SIRET 19751717000013."
        3. User: "What more can you tell me about this business?"
        4. Assistant: [Provides additional context by querying this tool for example, using the SIRET 19751717000013]
    
    Args:
    siret: The 14-digit SIRET number identifying the individual establishment to
        retrieve. The value should contain exactly 14 digits.

    Returns:
        A list of UniversityModel instances matching the provided SIRET.
    """
    instance = UniversityRequest()
    await instance()
    if instance._cached_response is None:
        return []
    data = filter_data(instance, siret=siret)
    data = [item for item in data if siret in item.get("siret", [])]
    return [UniversityModel(**item) for item in data]
