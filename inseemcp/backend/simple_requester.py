import os
from typing import Literal
from urllib.parse import urlencode

import httpx2
import pydantic
from pydantic import Field

from models.base import EstablishmentEnum, LegalUnitEnum

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
    nombre: str | None = Field(
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

class ResponsError(pydantic.BaseModel):
    status_code: int
    content: str


class Requester:
    base_url: str = 'https://api.insee.fr/api-sirene/3.11/{param}'

    def __init__(self, param: Literal['siren', 'siret'] = 'siren'):
        self._final_url: str = ''
        self.param = param
        self.error: ResponsError | None = None

    @property
    def has_error(self):
        return self.error is not None

    def url(self, search: SearchModel | MultiCriteriaSearchModel):
        initial_url = self.base_url.format(param=self.param)
        query_params = search.model_dump(exclude_none=True)
        if query_params:
            initial_url = initial_url + '?' + urlencode(query_params)
        return initial_url

    async def __call__(self, search: SearchModel | MultiCriteriaSearchModel) -> dict | None:
        api_key: str = os.environ.get('INSEE_API_KEY')
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            AUTHORIZATION_HEADER: api_key
        }

        if api_key is None:
            raise ValueError('INSEE_API_KEY environment variable is not set')

        async with httpx2.AsyncClient() as client:
            response = await client.get(self.url(search), headers=headers)
            if response.status_code != 200:
                self.error = ResponsError(
                    status_code=response.status_code,
                    content=response.json()
                )
            return response.json()
        return None


def inversion(value: str) -> str:
    return f'-{value}'


def wild_card(value: str) -> str:
    return f'{value}*'


def key_value_pair(key: str, value: str | None = None) -> str:
    if value is None:
        value = ''
    return f'{key}:{value}'


def condition_and(column: LegalUnitEnum | EstablishmentEnum, *values: str) -> str:
    key_value_pairs = [key_value_pair(column.value, value) for value in values]
    return ' AND '.join(key_value_pairs)


def condition_or(column: LegalUnitEnum | EstablishmentEnum, *values: str) -> str:
    key_value_pairs = [key_value_pair(column.value, value) for value in values]
    return ' OR '.join(key_value_pairs)


def condition_to(lhv: str, rhv: str) -> str:
    return f'({lhv} TO {rhv})'


def condition_period(value: str) -> str:
    return f'periode({value})'

