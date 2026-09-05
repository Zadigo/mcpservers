from fastmcp.tools import tool

from backend.simple_requester import (
    MultiCriteriaSearchModel,
    Requester,
    SearchModel,
    condition_period,
    inversion,
    join_operator,
    key_value_pair,
    wild_card,
)
from components.utils import select_response
from models.base import BusinessColumnEnum


@tool
async def get_siret(siret: str, date: str | None = None):
    """
    Search for a single SIRET number.

    Arguments:
        siret (str): The SIRET number to search for.
        date (str | None): The date of the SIRET number to search for.
    """
    instance = Requester(single_search=True, param='siret')
    await instance(SearchModel(date=date), url_param=siret)
    return select_response(instance)


@tool
async def get_siren_startswith(siren: str):
    """
    Search for all SIREN numbers that start with a specific string.

    Arguments:
        siren (str): The starting string of the SIREN numbers to search for.
    """
    instance = Requester(single_search=False, param='siren')

    str_query = wild_card(BusinessColumnEnum.SIREN, siren)
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

    query1 = wild_card(BusinessColumnEnum.NOM_UNITE_LEGALE, name)
    query2 = wild_card(BusinessColumnEnum.NOM_USAGE_UNITE_LEGALE, name)
        
    query = MultiCriteriaSearchModel(q=join_operator('OR', query1, query2))

    await instance(query)
    return select_response(instance)


@tool
async def legal_units_column_has_no_value(column_name: str):
    """
    Search for legal units where a specific column has no value.

    Arguments:
        column_name (str): The column to check for no value.
    """
    instance = Requester(single_search=False)
    str_query = inversion(wild_card(BusinessColumnEnum.__getitem__(column_name)))
    await instance(MultiCriteriaSearchModel(q=str_query))
    return select_response(instance)



@tool
async def legal_units_exact_search(column_name: str, value: str, count: int = 20, offset: int = 0):
    """
    Search for legal units where a specific column has an exact value.

    Arguments:
        column_name (str): The column to check for the exact value.
        value (str): The exact value to search for.
        count (int): The number of search results to return.
        offset (int): The offset for the search results.
    """
    instance = Requester(single_search=False)

    str_query = condition_period(key_value_pair(BusinessColumnEnum.__getitem__(column_name), value))
    await instance(MultiCriteriaSearchModel(q=str_query, debut=offset, nombre=count))
    return select_response(instance)
