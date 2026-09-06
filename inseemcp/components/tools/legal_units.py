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
async def get_legal_unit_name_startswith(name: str):
    """
    Search for all legal units where the legal unit's name starts with the specified string.
    This function performs a wildcard search on the columns `nomUniteLegale` and `nomUsageUniteLegale`.
    Refer to the `etablissement.md` resource documentation for more details on the column types and
    definitions.

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
async def get_legal_units_column_has_no_value(column_name: str):
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
    Search for legal units that match the given column and value. Use this function for arbitrary
    searches on any column of the legal units.

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


@tool
async def get_legal_units_by_name(name: str, postal_code: str | None = None, count: int = 20, offset: int = 0):
    """
    Search  for legal units by name and within the specificied location. This function is specialized
    for searching legal units by their name and should be used in priority when the user is searching
    for a specific name.

    Arguments:
        name (str): The name of the legal units to search for.
        postal_code (str | None): The postal code to filter the legal units by.
        count (int): The number of search results to return.
        offset (int): The offset for the search results.
    """
    instance = Requester(single_search=False, param='siret')

    str_query1 = key_value_pair(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, name)
    str_query2: str | None = None
    if postal_code is not None:
        str_query2 = key_value_pair(BusinessColumnEnum.CODE_POSTAL_ETABLISSEMENT, postal_code)

    str_query = join_operator('AND', str_query1, str_query2)
    await instance(MultiCriteriaSearchModel(q=str_query, debut=offset, nombre=count))
    return select_response(instance)
