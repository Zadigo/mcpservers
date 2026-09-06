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
async def get_siren_startswith(siren: str):
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

    Returns:
        Information about the legal units whose SIREN numbers start with the specified string.

    Raises:
        ValueError: If the SIREN has an invalid format.
        ...: If the INSEE API request fails.
    """
    instance = Requester(single_search=False, param='siren')

    str_query = wild_card(BusinessColumnEnum.SIREN, siren)
    query = MultiCriteriaSearchModel(q=str_query)

    await instance(query, url_param=siren)
    return select_response(instance)



@tool
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
async def search_establishments_name_startswith(name: str, postal_code: str | None = None):
    """
    Search INSEE enterprise data for establishments whose associated
    legal unit denomination starts with the specified text.

    Use this tool when the user wants to find establishments or companies
    by the beginning of their name.

    The search uses a wildcard prefix match against the INSEE legal-unit
    denomination. It can therefore return multiple establishments
    belonging to legal units whose names match the supplied prefix.

    Args:
        name: The beginning of the legal unit's denomination to search
            for. For example, "Michelin" searches for denominations
            beginning with "Michelin".
        postal_code: Optional[str]: Optional postal code to filter the establishments by.

    Returns:
        A collection of matching establishment records. Each result may
        contain establishment and legal-unit information returned by the
        INSEE API.

    Notes:
        - This is a prefix search, not an exact-name search.
        - Multiple establishments may be returned for the same legal unit.
        - The search is performed against the legal-unit denomination, not the establishment's SIRET.
        - An empty or very broad prefix may produce a large number of
          results.
    """
    instance = Requester(single_search=False, param='siret')

    str_query = wild_card(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, name)

    if postal_code is not None:
        str_query = join_operator('AND', str_query, wild_card(BusinessColumnEnum.CODE_POSTAL_ETABLISSEMENT, postal_code))

    query = MultiCriteriaSearchModel(q=str_query)

    await instance(query)
    return select_response(instance)
