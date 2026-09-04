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
    Search for a single SIREN number.

    Arguments:
        siren (str): The SIREN number to search for.
        date (str | None): The date of the SIREN number to search for.
    """
    instance = Requester(single_search=True)
    await instance(SearchModel(), url_param=siren)
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
async def search_establishments_name_startswith(name: str):
    """
    Search for establishments that start with a specific name.

    Arguments:
        name (str): The name of the establishments to search for.
    """
    instance = Requester(single_search=False, param='siret')
    query = MultiCriteriaSearchModel(q=wild_card(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, name))

    await instance(query)
    return select_response(instance)
