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
async def get_siren(siren: str, date: str | None = None):
    """
    Retrieve information about a specific French legal unit using its
    SIREN number from the INSEE enterprise data.

    A SIREN is a unique 9-digit identifier assigned to a legal unit
    (enterprise/company). It is different from a SIRET, which identifies
    an individual establishment belonging to that legal unit.

    Do not use this tool when:
    - the user provides a SIRET and wants information about an establishment;
    - the user wants to search for companies by name;
    - the user wants to find multiple SIRENs;
    - the user wants to find establishments belonging to a SIREN.

    Args:
        siren: The 9-digit SIREN number identifying the legal unit to
            retrieve. The value should contain exactly 9 digits.

        date: Optional date used to retrieve the state of the legal unit
            at a specific point in time. Use the date format expected by
            the INSEE API (YYYY-MM-DD). If omitted, the current/latest
            available information is returned.

    Returns:
        Information about the legal unit corresponding to the SIREN.
        If no legal unit exists for the supplied SIREN, the tool returns
        the corresponding INSEE API result rather than inventing data.

    Raises:
        ValueError: If the SIREN or date has an invalid format.
        ...: If the INSEE API request fails.
    """
    instance = Requester(single_search=True)
    await instance(SearchModel(date=date), url_param=siren)
    return select_response(instance)


@tool
async def get_siren_startswith(siren: str, date: str | None = None):
    """
    Retrieve information about French legal units whose SIREN numbers start with the specified string
    from the INSEE enterprise data.

    A SIREN is a unique 9-digit identifier assigned to a legal unit
    (enterprise/company). It is different from a SIRET, which identifies
    an individual establishment belonging to that legal unit.

    Do not use this tool when:
    - the user provides a SIRET and wants information about an establishment;
    - the user wants to search for companies by name;
    - the user wants to find multiple SIRENs;
    - the user wants to find establishments belonging to a SIREN.

    Indicate to the user the amount of results returned by the API, if available. If
    he wants to paginate to the next page of results or explore a partiular establishment
    by extracting the information of the current enterprise/company in the current list
    of establishments.

    Args:
        siren: The starting string of the SIREN numbers to search for.
        date: Optional date used to retrieve the state of the legal unit
            at a specific point in time. Use the date format expected by
            the INSEE API (YYYY-MM-DD). If omitted, the current/latest
            available information is returned.

    Returns:
        Information about the legal units whose SIREN numbers start with the specified string.

    Raises:
        ValueError: If the SIREN has an invalid format.
        ...: If the INSEE API request fails.
    """
    instance = Requester(single_search=False, param='siren')

    str_query = wild_card(BusinessColumnEnum.SIREN, siren)
    query = MultiCriteriaSearchModel(q=str_query, date=date)

    await instance(query, url_param=siren)
    return select_response(instance)


async def establishments_siren_not_start_by(siren: list[str]):
    """
    Search for establishments where the SIREN number does not start with the specified strings.

    Arguments:
        siren (list[str]): The list of starting strings of the SIREN numbers to exclude.
    """
    instance = Requester(single_search=False, param='siren')

    queries = [inversion(wild_card(BusinessColumnEnum.SIREN, s)) for s in siren]
    query = MultiCriteriaSearchModel(q=join_operator('AND', *queries))

    await instance(query)
    return select_response(instance)


@tool
async def get_legal_unit_name_startswith(name: str, date: str | None = None):
    """
    Search for all legal units where the legal unit's name starts with the specified string.
    This function performs a wildcard search on the columns `nomUniteLegale` and `nomUsageUniteLegale`.
    Refer to the `etablissement.md` resource documentation for more details on the column types and
    definitions.

    Notes:
        - The search is performed against the legal-unit name columns, not the establishment's SIRET.
        - An empty or very broad prefix may produce a large number of results.
        - The `date` parameter allows you to retrieve the state of the legal unit at a specific point in time.

    Arguments:
        name (str): The starting string of the legal unit names to search for.
        date: Optional date used to retrieve the state of the legal unit
            at a specific point in time. Use the date format expected by
            the INSEE API (YYYY-MM-DD). If omitted, the current/latest
            available information is returned.
    """
    instance = Requester(single_search=False, param='siren')

    query1 = wild_card(BusinessColumnEnum.NOM_UNITE_LEGALE, name)
    query2 = wild_card(BusinessColumnEnum.NOM_USAGE_UNITE_LEGALE, name)
        
    query = MultiCriteriaSearchModel(q=join_operator('OR', query1, query2), date=date)

    await instance(query)
    return select_response(instance)


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
async def get_legal_units_by_name_and_location(name: str, postal_code: str | None = None, date: str | None = None, count: int = 20, offset: int = 0):
    """
    Search  for legal units by name and within the specificied location. This function is specialized
    for searching legal units by their name and should be used in priority when the user is searching
    for a specific name.

    Args:
        name (str): The name of the legal units to search for.
        postal_code (str | None): The postal code to filter the legal units by.
        count (int): The number of search results to return.
        offset (int): The offset for the search results.
        date (str | None): Optional date used to retrieve the state of the legal unit at a specific point in time.
            Use the date format expected by the INSEE API (YYYY-MM-DD). If omitted, the current/latest available information is returned.

    Returns:
        A collection of matching legal unit records. Each result may contain legal unit information returned by the INSEE API.
    """
    instance = Requester(single_search=False, param='siret')

    str_query1 = key_value_pair(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, name)
    str_query2: str | None = None
    if postal_code is not None:
        str_query2 = key_value_pair(BusinessColumnEnum.CODE_POSTAL_ETABLISSEMENT, postal_code)

    str_query = join_operator('AND', str_query1, str_query2)
    await instance(MultiCriteriaSearchModel(q=str_query, debut=offset, nombre=count, date=date))
    return select_response(instance)


@tool
async def search_legal_units_by_address(street_name: str, postal_code: str | None = None, date: str | None = None, count: int = 20, offset: int = 0):
    """Search for legal units where the street name matches the provided value.

    When to use this tool:
        - Use this tool when the user provides a street name for where to find the legal units.

    Arguments:
        street_name (str): The street name to search for in the address of legal units.
        postal_code (str | None): The postal code to filter the legal units by.
        date (str | None): Optional date used to retrieve the state of the legal unit at a specific point in time.
            Use the date format expected by the INSEE API (YYYY-MM-DD). If omitted, the current/latest available information is returned.
        count (int): The number of search results to return.
        offset (int): The offset for the search results.
    """
    instance = Requester(single_search=False, param='siret')

    str_query1 = wild_card(BusinessColumnEnum.LIBELLE_VOIE_ETABLISSEMENT)
    str_query2 = wild_card(BusinessColumnEnum.LIBELLE_VOIE_ETABLISSEMENT, street_name, quote_value=True)
    str_query3 = key_value_pair(BusinessColumnEnum.CODE_POSTAL_ETABLISSEMENT, postal_code)

    str_query = join_operator('AND', str_query1, str_query2, str_query3)
    await instance(MultiCriteriaSearchModel(q=str_query, debut=offset, nombre=count, date=date))
    return select_response(instance)
