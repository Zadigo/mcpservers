from abc import ABC
from collections.abc import Sequence
from typing import Any

import httpx2
from pydantic import BaseModel

from backend.models import ResponseError

type TypeDataReturn[T = dict[str, Any]] = T | Sequence[T] | None

class BaseRequest(ABC):
    base_url: str | None = None
    cache_key: str = 'inseemcp:{value}'
    error: ResponseError | None = None
    _cached_response: httpx2.Response | None = None
    model: BaseModel | None = None

    def __init__(self) -> None:
        self.headers: dict[str, str] = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

    @property
    def url(self):
        return '' if self.base_url is None else self.base_url

    def clean(self, data: TypeDataReturn) -> TypeDataReturn:
        """Use the clean function to process the data before returning it.

        Args:
            data (TypeDataReturn): The data to be cleaned.

        Returns:
            TypeDataReturn: The cleaned data.
        """
        return data

    async def __call__(self, headers: dict[str, str] | None = None) -> TypeDataReturn:
        self.headers = headers or {} | self.headers

        if self.url == '':
            raise ValueError('The url does not have a valid format')

        async with httpx2.AsyncClient() as client:
            response = await client.get(self.url, headers=self.headers, timeout=30)
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
            return self.clean(self._cached_response.json())
