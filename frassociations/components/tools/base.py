import enum

from fastmcp.tools import tool
from fastmcp.tools.base import ToolResult
from pydantic import Field

from components.utils import dataframe_to_models, paginate
from models.results import AssociationModel
from utils import FilesQueryset


class SortOptions(enum.Enum):
    CREATION_DATE = "date_creat"
    TITLE = "titre"

@tool
async def search_dataset(
    limit: int = Field(default=100, gt=0, description="Number of results to return"),
    offset: int = Field(default=0, gte=0, description="Offset for pagination"),
    siret: str | None = Field(default=None, description="SIRET number to filter the results"),
    titre: str | None = Field(default=None, description="Title to filter the results"),
    has_website: bool | None = Field(default=None, description="Filter results based on the presence of a website"),
    sort_by: SortOptions | None = Field(default=SortOptions.CREATION_DATE, description="Field to sort the results by"),
    commune: str | None = Field(default=None, description="Commune to filter the results"),
) -> list[AssociationModel]:
    """
    Search for a dataset in the database.
    
    Args:
        limit (int): Number of results to return.
        offset (int): Offset for pagination.
        siret (str | None): SIRET number to filter the results.
        titre (str | None): Title to filter the results.
        has_website (bool | None): Filter results based on the presence of a website.
        commune (str | None): Commune to filter the results.
        sort_by (SortOptions | None): Field to sort the results by.
    """
    instance = FilesQueryset()
    df = await instance.prefetch_files()

    # Filter by commune if provided
    if commune is not None:
        df = df[~df['adrs_libcommune'].isna()]
        df = df[df['adrs_libcommune'].str.contains(commune, na=False, case=False)]

    # Has website
    if has_website is not None:
        if has_website:
            df = df[~df['siteweb'].isna()]
        else:
            df = df[df['siteweb'].isna()]

    # Filter by SIRET number if provided
    if siret is not None:
        df = df[~df['siret'].isna()]
        df = df[df['siret'].astype(str).str.contains(siret, na=False)]

    #  Search by title if provided
    if titre is not None:
        df = df[~df['titre'].isna() | ~df['titre_court'].isna() | ~df['objet'].isna()]

        df = df[
            df['titre'].str.contains(titre, na=False, case=False) |
            df['titre_court'].str.contains(titre, na=False, case=False) |
            df['objet'].str.contains(titre, na=False, case=False)
        ]

    # Sorting
    if sort_by is not None:
        df.sort_values(by=sort_by.value, inplace=True)

    # Pagination
    values, pagination_info = paginate(limit=limit, offset=offset, values=dataframe_to_models(df))

    return ToolResult(
        structured_content={
            'result': values
        },
        meta={
            'pagination': pagination_info.model_dump()
        }
    )
