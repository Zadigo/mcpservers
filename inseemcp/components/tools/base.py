from fastmcp.tools import ToolResult, tool
from pydantic import Field

from backend import query
from backend.base import (
    MultiCriteriaSearchLegalUnit,
    MultiCriteriaSearchQuery,
    SearchEstablishment,
    SearchLegalUnit,
    SingleSearchQuery,
)
from backend.operators import KeyValuePair
from models.base import EstablishmentEnum


@tool
async def get_siret(siret: str, date: str | None = Field(default=None, description="Date of the SIRET number to search for.")):
    """
    Search for a single SIRET number.

    Arguments:
        siret (str): The SIRET number to search for.
        date (str | None): The date of the SIRET number to search for.
    """
    instance = SearchEstablishment(SingleSearchQuery(siren_ou_siret=siret, date=date))
    response = await query(instance)
    return ToolResult(
        structured_content=response, 
        meta={
            "search_type_fr": "établissements",
            "url": instance.request._final_url
        }
    )


@tool
async def get_siren(siren: str, date: str | None = Field(default=None, description="Date of the SIREN number to search for.")):
    """
    Search for a single SIREN number.

    Arguments:
        siren (str): The SIREN number to search for.
        date (str | None): The date of the SIREN number to search for.
    """
    instance = SearchLegalUnit(SingleSearchQuery(siren_ou_siret=siren, date=date))
    response = await query(instance)
    return ToolResult(
        structured_content=response, 
        meta={
            "search_type_fr": "unités légales",
            "url": instance.request._final_url
        }
    )


@tool
async def get_siren_startswith(siren: str):
    """
    Search for all SIREN numbers that start with a specific string.

    Arguments:
        siren (str): The starting string of the SIREN numbers to search for.
    """
    kv = KeyValuePair(EstablishmentEnum.SIREN, value=siren)
    instance = MultiCriteriaSearchLegalUnit(query=MultiCriteriaSearchQuery(q=kv))
    response = await query(instance)
    
    return ToolResult(
        structured_content=response, 
        meta={
            "search_type_fr": "unités légales",
            "url": instance.request._final_url
        }
    )


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
async def search_for_establishments_by_activity_code(activity_code: str = Field(description="The activity code of the establishments to search for.")):
    """
    Search for establishments with a specific activity code.

    Arguments:
        activity_code (str): The activity code of the establishments to search for.
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
