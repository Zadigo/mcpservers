import os
from typing import Literal
from urllib.parse import urlencode

import httpx2
import pydantic
from pydantic import Field

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

class ResponseError(pydantic.BaseModel):
    status_code: int
    content: str
    json_content: dict | None = None


class Requester:
    base_url: str = 'https://api.insee.fr/api-sirene/3.11/{param}'
    single_search_url = 'https://api.insee.fr/api-sirene/3.11/{param}/{value}'

    def __init__(self, single_search: bool = True, param: Literal['siren', 'siret'] = 'siren'):
        self.single_search = single_search
        self._final_url: str = ''
        self.param = param
        self.error: ResponseError | None = None
        self._cached_response: dict | None = None

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
        api_key: str = os.environ.get('INSEE_API_KEY')
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
            response = await client.get(self._final_url, headers=headers)
            if response.status_code != 200:
                self.error = ResponseError(
                    status_code=response.status_code,
                    content=response.text,
                    json_content=response.json()
                )

            self._cached_response = response.json()
            return self._cached_response
        return None


def inversion(value: str) -> str:
    return f'-{value}'


def wild_card(key: BusinessColumnEnum, value: str | None = None) -> str:
    result = key_value_pair(key.value, value)
    return f'{result}*'


def key_value_pair(key: str | BusinessColumnEnum, value: str | None = None) -> str:
    if value is None:
        value = ''

    if isinstance(key, BusinessColumnEnum):
        key = key.value

    return f'{key}:{value}'


def join_operator(operator: Literal['AND', 'OR'], *values: str) -> str:
    return f' {operator} '.join(values)


def condition_and(column: BusinessColumnEnum, *values: str) -> str:
    key_value_pairs = [key_value_pair(column, value) for value in values]
    return join_operator('AND', *key_value_pairs)


def condition_or(column: BusinessColumnEnum, *values: str) -> str:
    key_value_pairs = [key_value_pair(column, value) for value in values]
    return join_operator('OR', *key_value_pairs)


def condition_or_dict(conditons: dict[BusinessColumnEnum, str]) -> str:
    values = []
    for key, value in conditons.items():
        if isinstance(key, str):
            values.append(key_value_pair(key, value))
        else:
            values.append(key_value_pair(key.value, value))

    return ' OR '.join(values)


def condition_to(lhv: str, rhv: str) -> str:
    return f'({lhv} TO {rhv})'


def condition_period(value: str) -> str:
    return f'periode({value})'



