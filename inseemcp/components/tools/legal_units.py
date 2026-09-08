from typing import Literal

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

type TypeState = Literal['all',  'active', 'ceased']

type TypeLegalUnitCategory = Literal['all', 'MIC', 'PME', 'ETI', 'GE']

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
async def search_legal_units_by_siren_prefix(
    siren_prefix: str,
    active_state: TypeState = "all",
    legal_unit_category: TypeLegalUnitCategory = "all",
    code_naf: str | None = None,
    date: str | None = None,
    offset: int = 0,
):
    """
    Search the INSEE enterprise data for French legal units whose SIREN
    starts with the specified prefix.

    A SIREN is a 9-digit identifier assigned to a legal unit. It is
    different from a SIRET, which identifies an individual establishment
    belonging to a legal unit.

    Use this tool for prefix-based searches that may return multiple
    legal units.

    Do not use this tool when:
    - the user provides a SIRET;
    - the user wants to search legal units by name;
    - the user wants information about one specific SIREN;
    - the user wants to search for establishments or SIRETs.

    Pagination:
    - The API returns pagination metadata including the total number of
    matching results, the current offset, and the number of results returned.
    - Do not retrieve every matching result automatically when the total
    result count is large.
    - Present the current page and report the total number of matches.
    - If the user requests additional results, use the `offset` parameter
    to retrieve the next page.
    - When the result set is very large, suggest narrowing the search with
    a more specific SIREN prefix or one of the available filters.

    When results are paginated, clearly distinguish the total number of
    matching legal units from the number returned in the current response.

    If the result set is large, suggest narrowing the search using:
    - a longer SIREN prefix;
    - the active state;
    - the legal unit category;
    - the NAF activity code.

    Args:
        siren_prefix:
            The beginning of the SIREN to search for. This is a prefix,
            not necessarily a complete 9-digit SIREN.

        active_state:
            Filter by the legal unit's active state. Defaults to "all".

        legal_unit_category:
            Filter by legal unit category. Defaults to "all".

        code_naf:
            Optional NAF activity code used to filter the legal units.

        date:
            Optional date used to retrieve information corresponding to
            a specific point in time. The date must use the format
            expected by the INSEE API (YYYY-MM-DD).

        offset:
            Number of matching results to skip before returning results.
            Use this parameter to paginate through the result set.
            Defaults to 0.

    Returns:
        Matching French legal units, including their SIREN and the
        information provided by the INSEE enterprise API.

    Raises:
        ValueError:
            If the SIREN prefix, date, or another parameter has an
            invalid format.

        ...:
            If the INSEE API request fails.
    """
    instance = Requester(single_search=False, param='siren')

    str_query = wild_card(BusinessColumnEnum.SIREN, siren_prefix)
    and_query: list[str | None] = []

    _state: str | None = None
    match active_state:
        case 'active':
            _state = 'A'
            
        case 'ceased':
            _state = 'C'
        case _:
            pass

    result = key_value_pair(BusinessColumnEnum.ETAT_ADMINISTRATIF_UNITE_LEGALE, _state, allow_none=True)
    if result is not None:
        and_query.append(condition_period(result))

    if legal_unit_category != 'all':
        result = key_value_pair(BusinessColumnEnum.CATEGORIE_ENTREPRISE, legal_unit_category, allow_none=True)
        if result is not None:
            and_query.append(result)

    result = key_value_pair(BusinessColumnEnum.ACTIVITE_PRINCIPALE_NAF25_ETABLISSEMENT, code_naf, allow_none=True)
    if result is not None:
        and_query.append(result)

    if and_query:
        str_query = join_operator('AND', str_query, *and_query)

    query = MultiCriteriaSearchModel(q=str_query, date=date, debut=offset)
    await instance(query)
    return select_response(instance)


@tool
async def search_legal_units_by_name_prefix(name: str, exact_search: bool = False, date: str | None = None):
    """
    Search the INSEE enterprise data for French legal units whose name
    starts with the specified prefix.

    The search considers multiple legal-unit name and denomination fields,
    including official names, usage names and usual denominations. This
    allows the tool to find legal units when the user provides an
    abbreviated, shortened or alternative form of the name.

    For example, a search for "CCM PONT L'ABBE" may match a legal unit
    whose official denomination is "CAISSE CREDIT MUTUEL PONT L'ABBE".

    Use this tool when:
    - the user wants to find one or more legal units by name;
    - the user provides only part of a legal-unit name;
    - the user provides an abbreviated or commonly used name;
    - the exact legal-unit name is uncertain.

    Do not use this tool when:
    - the user provides a SIREN and wants information about that
      specific legal unit;
    - the user provides a SIRET;
    - the user wants to search establishments by name;
    - the user wants to search using a SIREN prefix.

    Name matching is based on the beginning of the relevant name or
    denomination field. Names are not unique identifiers, so multiple
    legal units may be returned.

    When multiple results are returned, use the available information
    such as SIREN, name, denomination and location to help identify the
    most relevant legal unit. Do not assume that a matching name
    uniquely identifies a legal unit.

    Args:
        name_prefix:
            Beginning of the legal-unit name or denomination to search
            for. The value may be an abbreviated or commonly used name.

        date:
            Optional date used to retrieve information corresponding to
            a specific point in time. Format: YYYY-MM-DD.

    Returns:
        Matching legal units from the INSEE enterprise data.

    Raises:
        ValueError:
            If an input parameter has an invalid format.

        ...:
            If the INSEE API request fails.
    """
    instance = Requester(single_search=False, param='siren')

    str_q1 = condition_period(wild_card(BusinessColumnEnum.NOM_UNITE_LEGALE))
    str_q2 = condition_period(wild_card(BusinessColumnEnum.NOM_UNITE_LEGALE, name))
    str_q3 = condition_period(wild_card(BusinessColumnEnum.NOM_USAGE_UNITE_LEGALE, name))
    str_q4 = condition_period(wild_card(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, name))
    str_q5 = condition_period(wild_card(BusinessColumnEnum.DENOMINATION_USUELLE_UNITE_LEGALE, name))
    str_q6 = condition_period(wild_card(BusinessColumnEnum.DENOMINATION_USUELLE1_UNITE_LEGALE, name))
    str_q7 = condition_period(wild_card(BusinessColumnEnum.DENOMINATION_USUELLE2_UNITE_LEGALE, name))
    str_q8 = condition_period(wild_card(BusinessColumnEnum.DENOMINATION_USUELLE3_UNITE_LEGALE, name))

    query = join_operator('OR', str_q2, str_q3, str_q4, str_q5, str_q6, str_q7, str_q8)
    query = join_operator('AND', str_q1, query)
    query = MultiCriteriaSearchModel(q=query, date=date)

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
    str_query2 = key_value_pair(BusinessColumnEnum.CODE_POSTAL_ETABLISSEMENT, value=postal_code, allow_none=True)
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
    str_query3 = key_value_pair(BusinessColumnEnum.CODE_POSTAL_ETABLISSEMENT, postal_code, allow_none=True)
    str_query = join_operator('AND', str_query1, str_query2, str_query3)

    await instance(MultiCriteriaSearchModel(q=str_query, debut=offset, nombre=count, date=date))
    return select_response(instance)
