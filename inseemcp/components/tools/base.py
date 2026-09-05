from fastmcp.tools import ToolResult, tool

from backend.simple_requester import (
    MultiCriteriaSearchModel,
    Requester,
    condition_and,
    condition_or,
    condition_period,
)
from models.base import BaseResponseModel, BusinessColumnEnum
from utils import logger


@tool
async def search_entreprises_by_activity_codes(
    activity_codes: list[str] = (),
    inclusive: bool = True
) -> BaseResponseModel:
    """
    Search for entreprises with a specific activity code.

    Arguments:
        activity_codes (list[str]): The activity codes of the entreprises to search for.
        inclusive (bool): Whether to include entreprises with any of the activity codes (True) or all of them (False).
    """
    instance = Requester(single_search=False)

    if len(activity_codes) == 0:
        return ToolResult(content="No activity codes provided.", is_error=True)

    str_query: str = ""
    if len(activity_codes) == 1:
        str_query = activity_codes[0]
    else:
        and_conditions = condition_and(BusinessColumnEnum.ACTIVITE_PRINCIPALE_UNITE_LEGALE, *activity_codes)
        or_conditions = condition_or(BusinessColumnEnum.ACTIVITE_PRINCIPALE_UNITE_LEGALE, *activity_codes)
        str_query: str = and_conditions if inclusive else or_conditions

    query = MultiCriteriaSearchModel(q=condition_period(str_query))
    response = await instance(query)

    if instance.has_error:
        logger.error(f"Error occurred while searching for entreprises by activity codes: {instance.error.content}")
        return ToolResult(content=instance.error.content, is_error=True)

    return ToolResult(
        structured_content=response, 
        meta={
            "search_type_fr": "entreprises",
            "url": instance._final_url
        }
    )
