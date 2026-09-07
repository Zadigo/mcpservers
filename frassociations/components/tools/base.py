import enum

from fastmcp.tools import tool

from components.utils import dataframe_to_models, paginate
from models.results import ResponseModel
from utils import FilesQueryset


class SortOptions(enum.Enum):
    CREATION_DATE = "date_creat"
    TITLE = "titre"


@tool
async def get_association_by_title(
    title: str,
    commune: str | None = None,
    siret: str | None = None,
    sort_by: SortOptions | None = SortOptions.CREATION_DATE,
    limit: int = 50,
    offset: int = 0,
) -> ResponseModel:
    """
    Return a list of association models matching its title. Additional
    search options include commune and SIRET number.

    Use this tool when the user is looking for assocations that match a 
    specific title. The match can be an exact or partial match.

    Instructions
        * Prefer this tool for name searching
        * 
    
    Args:
        title (str): Title to filter the results.
        commune (str | None): Commune to filter the results.
        sort_by (SortOptions | None): Field to sort the results by.
        siret (str | None): SIRET number to filter the results.
        limit (int): Number of results to return.
        offset (int): Offset for pagination.
        siret (str | None): SIRET number to filter the results.

    Returns:
        ResponseModel: Response model containing the list of association models matching the search criteria.
    """
    instance = FilesQueryset()
    df = await instance.prefetch_files()

    # Filter by title if provided
    df = df[
        ~df['titre'].isna() | 
        ~df['titre_court'].isna() | 
        ~df['objet'].isna()
    ]

    df = df[
        df['titre'].str.contains(title.casefold(), na=False, case=False) |
        df['titre_court'].str.contains(title.casefold(), na=False, case=False) |
        df['objet'].str.contains(title.casefold(), na=False, case=False)
    ]

    # Filter by commune if provided
    if commune is not None:
        df = df[~df['adrs_libcommune'].isna()]
        df = df[df['adrs_libcommune'].str.contains(commune.casefold(), na=False, case=False)]

    # Filter by SIRET number if provided
    if siret is not None:
        df = df[~df['siret'].isna()]
        df = df[df['siret'].astype(str).str.contains(siret, na=False)]

    # Sorting
    if sort_by is not None:
        df.sort_values(by=sort_by.value, inplace=True)

    values, _ = paginate(limit=limit, offset=offset, values=dataframe_to_models(df))
    return ResponseModel(total=len(df), offset=offset, results=values)


@tool
async def get_association_by_siret(siret: str) -> ResponseModel:
    """
    Return a list of association models matching the given SIRET number.

    A SIRET number is a a unique 14-digit code used by the French government to 
    identify a specific physical establishment of a business

    When to not use this tool:
    * For partial matches it is intended for exact SIRET number searches.

    Args:
        siret (str): SIRET number to filter the results.

    Returns:
        ResponseModel: Response model containing the list of association models matching the search criteria.
    """
    instance = FilesQueryset()
    df = await instance.prefetch_files()

    df = df[~df['siret'].isna()]
    df = df[df['siret'].astype(str).str.contains(siret, na=False)]

    values, _ = paginate(limit=len(df), offset=0, values=dataframe_to_models(df))
    return ResponseModel(total=len(df), offset=0, results=values)


@tool
async def get_associations_by_postal_code(postal_code: str) -> ResponseModel:
    """
    Return a list of association models matching the given postal code.

    A postal code is used to identify a specific geographic area for mail delivery
    and is a 5-digit number such as 75001.

    Instructions:
    * The postal code can be a five-digit number or,
    * A valid two-digit number representing the department code (e.g., 75 for Paris).

    Args:
        postal_code (str): Postal code to filter the results.

    Returns:
        ResponseModel: Response model containing the list of association models matching the search criteria.
    """
    instance = FilesQueryset()
    df = await instance.prefetch_files()

    df = df[~df['adrs_codepostal'].isna()]
    df = df[df['adrs_codepostal'].astype(str).str.contains(postal_code, na=False)]

    values, _ = paginate(limit=50, offset=0, values=dataframe_to_models(df))
    return ResponseModel(total=df.titre.count(), offset=0, results=values)
