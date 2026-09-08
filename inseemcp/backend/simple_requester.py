import os
from typing import Literal
from urllib.parse import urlencode

import httpx2
import pydantic
from pydantic import Field

from backend.models import ResponseError
from models.base import BusinessColumnEnum

AUTHORIZATION_HEADER: str = 'X-INSEE-Api-Key-Integration'

class QueryModel(pydantic.BaseModel):
    date: str | None = Field(
        default=None,
        description="Date for the multi-criteria search"
    )


class SearchModel(QueryModel):
    pass


class MultiCriteriaSearchModel(QueryModel):
    q: str | None = Field(
        default=None,
        description="Query string for the request"
    )
    tri: str | None = Field(
        default=None,
        description="Sorting criteria for the multi-criteria search"
    )
    nombre: int = Field(
        default=20,
        le=20,
        ge=1,
        description="Number of results for the multi-criteria search"
    )
    debut: int = Field(
        default=0,
        ge=0,
        description="Starting index for the multi-criteria search"
    )
    curseur: str | None = Field(
        default=None,
        description="Cursor for the multi-criteria search"
    )


class Requester:
    base_url: str = 'https://api.insee.fr/api-sirene/3.11/{param}'
    single_search_url = 'https://api.insee.fr/api-sirene/3.11/{param}/{value}'

    def __init__(self, single_search: bool = True, param: Literal['siren', 'siret'] = 'siren'):
        self.single_search = single_search
        self._final_url: str = ''
        self.param = param
        self.error: ResponseError | None = None
        self._cached_response: httpx2.Response | None = None

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: [{self._final_url}]>'

    @property
    def has_error(self):
        return self.error is not None

    def url(self, search: SearchModel | MultiCriteriaSearchModel, url_param: str | None = None):
        if self.single_search:
            url_param = url_param or ''

            if not url_param:
                raise ValueError(f"URL parameter '{self.param}' is required for single search")

            initial_url = self.single_search_url.format(param=self.param, value=url_param)
        else:
            initial_url = self.base_url.format(param=self.param)

        query_params = search.model_dump(exclude_none=True)
        if query_params:
            initial_url = initial_url + '?' + urlencode(query_params)
        return initial_url

    async def __call__(self, search: SearchModel | MultiCriteriaSearchModel, url_param: str | None = None, testing: bool = False) -> dict | None:
        """Sends a request to the INSEE API based on the search model and URL parameter.
        
        Args:
            search (SearchModel | MultiCriteriaSearchModel): The search model containing the query parameters.
            url_param (str | None): The URL parameter for single search. Required if single_search is True, otherwise ignored.
            testing (bool): If True, returns the URL and headers without making the actual request.

        Returns:
            dict | None: The JSON response from the INSEE API, or None if an error occurred or if testing is True.
        """

        api_key: str | None = os.environ.get('INSEE_API_KEY')
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            AUTHORIZATION_HEADER: api_key
        }

        if api_key is None:
            raise ValueError('INSEE_API_KEY environment variable is not set')

        self._final_url = self.url(search, url_param=url_param)
        if testing:
            return {"url": self._final_url, "headers": headers} 

        async with httpx2.AsyncClient() as client:
            response = await client.get(self._final_url, headers=headers, timeout=30)
            if response.status_code == 404:
                self.error = ResponseError(
                    status_code=response.status_code,
                    content="The requested resource was not found",
                    json_content=response.json()
                )
                return None

            if response.status_code != 200:
                self.error = ResponseError(
                    status_code=response.status_code,
                    content=response.text,
                    json_content=response.json()
                )

            self._cached_response = response
            return self._cached_response.json()
        return None


def inversion(value: str) -> str:
    """Inverts the given value by prefixing it with a minus sign.
    This is equivalent to negating the value in a query context.

    .. code-block:: python

        # Example: -value
        inversion("value")

    Args:
        value (str): The value to invert.

    Returns:
        str: The inverted value, prefixed with a minus sign.
    """
    return f'-{value}'


def wild_card(key: BusinessColumnEnum, value: str | None = None, quote_value: bool = False) -> str:
    """Returns a wildcard key-value paired query string formatted for the given key and optional value.

    .. code-block:: python
        # Use value as None to indicate that the field should have a
        # value:  denominationUniteLegale:* (should not be empty)
        wild_card(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE)

        # denominationUniteLegale:lecl*
        wild_card(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, "lecl")
    
    Args:
        key (BusinessColumnEnum): The key for the query.
        value (str | None): The value for the query. If None, only the key is used.
        quote_value (bool): Whether to quote the value in the query.

    Returns:
        str: The formatted wildcard query string.
    """
    if value is not None:
        if value.startswith('period'):
            raise ValueError("Wildcard value cannot start with 'period'")

        if 'AND' in value or 'OR' in value:
            raise ValueError("Wildcard value cannot contain 'AND' or 'OR'")

    result = key_value_pair(key.value, value, quote_value=quote_value)
    if result is not None:
        result = result.removesuffix('*')
    return f'{result}*'


def key_value_pair(key: str | BusinessColumnEnum, value: str | None = None, allow_none: bool = False, quote_value: bool = False) -> str | None:
    """Creates a key-value paired query string formatted for the given key and value.

    .. code-block:: python

        # denominationUniteLegale:leclerc
        key_value_pair(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, "leclerc")

        # Some values need to be quoted e.g. denominationUniteLegale:"leclerc"
        key_value_pair(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, "leclerc", quote_value=True)

    Args:
        key (str | BusinessColumnEnum): The key for the query.
        value (str | None): The value for the query. If None, only the key is used.
        allow_none (bool): Whether to ignore the value if it is None.
        quote_value (bool): Whether to quote the value in the query.

    Returns:
        str | None: The formatted key-value paired query string, or None if allowed and value is None.
    """
    if value is None and allow_none:
        return None
    
    if value is None:
        value = ''

    if quote_value and value is not None:
        value = f'"{value}"'

    if isinstance(key, BusinessColumnEnum):
        key = key.value

    return f'{key}:{value}'


def join_operator(operator: Literal['AND', 'OR'], *values: str | None) -> str:
    """Joins a set of query parameters with an AND or OR operator
    
    .. code-block:: python

        # Example: value1 AND value2
        join_operator('AND', 'value1', 'value2')

        # Example: value1 OR value2
        join_operator('OR', 'value1', 'value2')

    Args:
        operator (Literal['AND', 'OR']): The logical operator to join the values with.
        *values (str | None): The values to be joined.

    Returns:
        str: The joined query string using the specified operator.
    """
    return f' {operator} '.join([v for v in values if v is not None])


def condition_and(column: BusinessColumnEnum, *values: str) -> str:
    """Creates an AND condition for the given column and values.
    
    .. code-block:: python

        # Example: denominationUniteLegale:leclerc AND denominationUniteLegale:carrefour
        condition_and(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, "leclerc", "carrefour")

    Args:
        column (BusinessColumnEnum): The column for the query.
        *values (str): The values to be combined with the AND operator.

    Returns:
        str: The AND condition string combining the column and values.
    """
    key_value_pairs = [key_value_pair(column, value) for value in values]
    return join_operator('AND', *key_value_pairs)


def condition_or(column: BusinessColumnEnum, *values: str) -> str:
    """Creates an OR condition for the given column and values.

    .. code-block:: python

        # Example: denominationUniteLegale:leclerc OR denominationUniteLegale:carrefour
        condition_or(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, "leclerc", "carrefour")

    Args:
        column (BusinessColumnEnum): The column for the query.
        *values (str): The values to be combined with the OR operator.

    Returns:
        str: The OR condition string combining the column and values.
        condition_or(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, "leclerc", "carrefour")
    """
    key_value_pairs = [key_value_pair(column, value) for value in values]
    return join_operator('OR', *key_value_pairs)


def condition_or_dict(conditions: dict[BusinessColumnEnum, str]) -> str:
    """Creates an OR condition from a dictionary of column-value pairs."""
    values = []
    for key, value in conditions.items():
        if isinstance(key, str):
            values.append(key_value_pair(key, value))
        else:
            values.append(key_value_pair(key.value, value))

    return ' OR '.join(values)


def condition_to(start: str, end: str) -> str:
    """Creates a range condition for the given start and end values.

    .. code-block:: python

        # Example: [denominationUniteLegale:A TO denominationUniteLegale:C]
        condition_to("denominationUniteLegale:A", "denominationUniteLegale:C")

    Args:
        start (str): The start value of the range.
        end (str): The end value of the range.

    Returns:
        str: The range condition string in the format "[start TO end]".
    """
    return f'[{start} TO {end}]'


def condition_period(value: str | None) -> str:
    """Creates a period condition for the given value.

    Args:
        value (str | None): The value for the period condition.

    Returns:
        str: The period condition string in the format "periode(value)".
             Returns an empty string if the value is None.
    """
    if value is None:
        return ''
    return f'periode({value})'



