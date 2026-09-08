import asyncio
import json
import pathlib
import secrets

import aiofile
from fastmcp import Client
from fastmcp.tools import tool
from fastmcp.utilities.types import File

from backend.simple_requester import (
    MultiCriteriaSearchModel,
    Requester,
    SearchModel,
    join_operator,
    key_value_pair,
    wild_card,
)
from components.utils import select_response
from models.base import BaseResponseModel, BusinessColumnEnum
from utils import get_redis


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


@tool
async def search_establishments_by_code_naf(code_naf: str, postal_code: str | None = None, offset: int = 0):
    """
    Search INSEE enterprise data for establishments associated with a specific NAF code.

    A NAF code (Nomenclature d'Activités Française) represents the primary business activity of 
    a legal unit. This tool allows users to find establishments based on their associated NAF code.

    The NAF code is a 6-character alphanumeric code that classifies the primary 
    business activity of a legal unit. For example "62.01Z" represents computer 
    programming activities.

    INSEE assigns each French commune a 5-character code (generally 2 digits for the department and 3 digits for the commune).

    When to use this tool:
        - Use this tool when you need to find establishments based on their primary business activity.
        - The tool can be combined with postal code filtering to narrow down results geographically.

    How to use this tool:
        - Always ensure that the user provides a full NAF code (not a partial code).
        - The postal code can be a partial code (e.g. 59, 75, etc.) or a complete code (e.g. 59000, 75001, etc.).

    Args:
        code_naf: The NAF code to search for.
        postal_code: Optional postal code to filter the establishments by.
        offset: The starting point for pagination.

    Returns:
        A collection of matching establishment records. Each result may
        contain establishment and legal-unit information returned by the
        INSEE API.
    """
    instance = Requester(single_search=False, param='siret')

    str_query = key_value_pair(BusinessColumnEnum.ACTIVITE_PRINCIPALE_NAF25_ETABLISSEMENT, code_naf, quote_value=True)

    if postal_code is not None:
        str_query = join_operator('AND', str_query, wild_card(BusinessColumnEnum.CODE_POSTAL_ETABLISSEMENT, postal_code))

    query = MultiCriteriaSearchModel(q=str_query, debut=offset, nombre=20)

    await instance(query)
    return select_response(instance)


async def paginate_establishments(siren: str):
    """
    Paginate through establishments associated with a specific SIREN number.

    Arguments:
        siren (str): The SIREN number of the legal unit to retrieve establishments for.

    Returns:
        A collection of establishment records associated with the specified SIREN number. Each result may
        contain establishment and legal-unit information returned by the INSEE API.
    """
    from app import mcp


    job_id: str = secrets.token_hex(16)
    cache_key: str = f"inseemcp:{job_id}"

    redis_client = get_redis()

    instance = Requester(single_search=False, param='siret')
    async with Client(mcp, mode="auto") as client:
        # Initial query to get the first page of results
        str_query = key_value_pair(BusinessColumnEnum.SIREN, siren)
        query = MultiCriteriaSearchModel(q=str_query, debut=0, nombre=20)
        await instance(query)

        if instance._cached_response is not None:
            results = BaseResponseModel(**instance._cached_response.json())

            current_offset: int = 0
            number_of_pages: int = (results.header.total + 20 - 1) // 20

            while current_offset < number_of_pages * 20:
                str_query = key_value_pair(BusinessColumnEnum.SIREN, siren)
                query = MultiCriteriaSearchModel(q=str_query, debut=current_offset, nombre=20)
                await instance(query)

                # Push the results of each page to the Redis list
                other_responses = BaseResponseModel(**instance._cached_response.json())
                redis_client.lpush(cache_key, [json.dumps(item.model_dump(mode='json')) for item in other_responses.etablissements]) # pyright: ignore[reportArgumentType]

                current_offset += 20
                await asyncio.sleep(5)

        results = []
        while redis_client.llen(cache_key) > 0:
            page_content = redis_client.rpop(cache_key)
            if page_content:
                results.extend(json.loads(page_content)) # pyright: ignore[reportArgumentType]

    fullpath = pathlib.Path(f'./tmp/establishments_{job_id}.json')
    async with aiofile.async_open(fullpath, 'w') as f:
        await f.write(json.dumps(results))

        redis_client.delete(cache_key)
        async with aiofile.async_open(fullpath, 'rb') as f:
            data = await f.read()
            
            return File(
                path=fullpath, 
                data=data, 
                format='json'
            )
