from fastmcp.tools import tool

from backend.simple_requester import (
    MultiCriteriaSearchModel,
    Requester,
    SearchModel,
    inversion,
    join_operator,
    wild_card,
)
from components.utils import select_response
from models.base import EstablishmentEnum, LegalUnitEnum


@tool
async def get_siret(siret: str, date: str | None = None):
    """
    Search for a single SIRET number.

    Arguments:
        siret (str): The SIRET number to search for.
        date (str | None): The date of the SIRET number to search for.
    """
    instance = Requester(single_search=True, param='siret')
    await instance(SearchModel(), url_param=siret)
    return select_response(instance)


@tool
async def get_siren_startswith(siren: str):
    """
    Search for all SIREN numbers that start with a specific string.

    Arguments:
        siren (str): The starting string of the SIREN numbers to search for.
    """
    instance = Requester(single_search=False, param='siren')

    str_query = wild_card(EstablishmentEnum.SIREN, siren)
    query = MultiCriteriaSearchModel(q=str_query)

    await instance(query, url_param=siren)
    return select_response(instance)


@tool
async def get_legal_unit_name_startswith(name: str):
    """
    Search for all legal units where a specific column's value starts with a specific string.

    Arguments:
        name (str): The starting string of the legal unit names to search for.
    """
    instance = Requester(single_search=False, param='siren')

    query1 = wild_card(LegalUnitEnum.NOM_UNITE_LEGALE, name)
    query2 = wild_card(LegalUnitEnum.NOM_USAGE_UNITE_LEGALE, name)
        
    query = MultiCriteriaSearchModel(q=join_operator('OR', query1, query2))

    await instance(query)
    return select_response(instance)


@tool
async def legal_units_column_has_no_value(column: str):
    """
    Search for legal units where a specific column has no value.

    Arguments:
        column (str): The column to check for no value.
    """
    instance = Requester(single_search=False)
    str_query = inversion(wild_card(LegalUnitEnum.__getattr__(column)))
    await instance(MultiCriteriaSearchModel(q=str_query))
    return select_response(instance)
