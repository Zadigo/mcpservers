from fastmcp.tools import ToolResult, tool

from backend.simple_requester import (
    MultiCriteriaSearchModel,
    Requester,
    SearchModel,
    condition_and,
    condition_or,
    condition_period,
    select_response,
    wild_card,
)
from models.base import BaseResponseModel, LegalUnitEnum
from utils import logger


@tool
async def get_siret(siret: str, date: str | None = None):
    """
    Search for a single SIRET number.

    Arguments:
        siret (str): The SIRET number to search for.
        date (str | None): The date of the SIRET number to search for.
    """
    instance = Requester(siret=siret)
    query = SearchModel(date=date)

    await instance(query)
    return select_response(instance)


@tool
async def search_legal_units_by_activity_codes(
    activity_codes: list[str] = (),
    inclusive: bool = True
) -> BaseResponseModel:
    """
    Search for legal units with a specific activity code.

    Arguments:
        activity_codes (list[str]): The activity codes of the legal units to search for.
        inclusive (bool): Whether to include legal units with any of the activity codes (True) or all of them (False).
    """
    instance = Requester()

    if len(activity_codes) == 0:
        return ToolResult(content="No activity codes provided.", is_error=True)

    str_query: str = ""
    if len(activity_codes) == 1:
        str_query = activity_codes[0]
    else:
        and_conditions = condition_and(LegalUnitEnum.ACTIVITE_PRINCIPALE_UNITE_LEGALE, *activity_codes)
        or_conditions = condition_or(LegalUnitEnum.ACTIVITE_PRINCIPALE_UNITE_LEGALE, *activity_codes)
        str_query: str = and_conditions if inclusive else or_conditions

    query = MultiCriteriaSearchModel(q=condition_period(str_query))
    response = await instance(query)

    if instance.has_error:
        logger.error(f"Error occurred while searching for legal units by activity codes: {instance.error.content}")
        return ToolResult(content=instance.error.content, is_error=True)

    return ToolResult(
        structured_content=response, 
        meta={
            "search_type_fr": "unités légales",
            "url": instance._final_url
        }
    )


@tool
async def get_siren_startswith(siren: str):
    """
    Search for all SIREN numbers that start with a specific string.

    Arguments:
        siren (str): The starting string of the SIREN numbers to search for.
    """
    instance = Requester()

    str_query = wild_card(LegalUnitEnum.SIREN, siren)
    query = MultiCriteriaSearchModel(q=str_query)

    await instance(query)
    return select_response(instance)


# @tool
# async def legal_units_name_starts_with(name: str):
#     """
#     Search for all legal units with names that start with a specific string.

#     Arguments:
#         name (str): The starting string of the legal unit names to search for.
#     """
#     instance = Requester()

#     str_query = wild_card(LegalUnitEnum.DENOMINATION_UNITE_LEGALE, name)
#     query = MultiCriteriaSearchModel(q=str_query)

#     await instance(query)
#     return select_response(instance)
