from fastmcp.tools import tool
from pydantic import Field

from backend.simple_requester import (
    MultiCriteriaSearchModel,
    Requester,
    select_response,
    wild_card,
)
from models.base import EstablishmentEnum


@tool
async def get_siren(siren: str, date: str | None = None):
    """
    Search for a single SIREN number.

    Arguments:
        siren (str): The SIREN number to search for.
        date (str | None): The date of the SIREN number to search for.
    """
    instance = Requester()

    str_query = wild_card(EstablishmentEnum.SIREN, siren)
    query = MultiCriteriaSearchModel(q=str_query, date=date)

    await instance(query)
    return select_response(instance)


@tool
async def search_all_purged_legal_units():
    """
    Search for all purged legal units.
    """


@tool
async def search_all_purged_establishments():
    """
    Search for all purged establishments.
    """


@tool
async def search_all_establishments_within_commune(commune_code: str):
    """
    Search for all establishments within a specific "commune". A "commune" is the smallest administrative 
    division in France, similar to a municipality or township.

    Arguments:
        commune_code (str): The code of the commune to search for establishments.
    """


@tool
async def search_for_establishments_by_name(name: str):
    """
    Search for establishments with a specific name.

    Arguments:
        name (str): The name of the establishments to search for.
    """




@tool
async def search_for_terminated_legal_units():
    """
    Search for all terminated legal units.
    """


@tool
async def search_for_establishments_where_legal_unit_is_person():
    """
    Search for all establishments where the legal unit is a person.
    """


@tool
async def search_for_establishments_never_closed():
    """
    Search for all establishments that have never been c    losed.
    """


COLUMNS = Field(default=None, description="The columns to search in.")

@tool
async def multisearch(
    columns: list[str] | None = COLUMNS,
):
    """
    Perform an arbitrary search on the dataset
    """
