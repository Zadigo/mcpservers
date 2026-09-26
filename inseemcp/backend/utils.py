import datetime
import secrets
from abc import ABC
from collections.abc import Sequence
from typing import Any

import httpx2
import pandas
from pydantic import BaseModel

from backend.models import ResponseErrorModel
from utils import DATA_DIR

type TypeDataReturn[T = dict[str, Any]] = T | Sequence[T] | None

class BaseRequest[T = BaseModel](ABC):
    base_url: str | None = None
    cache_key: str = 'inseemcp:{value}'
    error: ResponseErrorModel | None = None
    _cached_response: httpx2.Response | None = None
    model: type[T] | None = None

    def __init__(self) -> None:
        self.headers: dict[str, str] = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

    @property
    def url(self):
        return '' if self.base_url is None else self.base_url

    @property
    def dataframe(self):
        if self._cached_response is None:
            return pandas.DataFrame()
        
        cleaned_data = self.clean(self._cached_response.json())
        return pandas.DataFrame(cleaned_data)

    def clean(self, data: TypeDataReturn) -> TypeDataReturn:
        """Use the clean function to process the data before returning it.

        Args:
            data (TypeDataReturn): The data to be cleaned.

        Returns:
            TypeDataReturn: The cleaned data.
        """
        return data

    async def __call__(self, headers: dict[str, str] | None = None, query: BaseModel | None = None) -> TypeDataReturn:
        self.headers = headers or {} | self.headers

        if self.url == '':
            raise ValueError('The url does not have a valid format')

        async with httpx2.AsyncClient() as client:
            params = query.model_dump(exclude_none=True) if query is not None else None
            response = await client.get(self.url, headers=self.headers, params=params, timeout=30)
            if response.status_code == 404:
                self.error = ResponseErrorModel(
                    status_code=response.status_code,
                    content="The requested resource was not found",
                    json_content=response.json()
                )
                return

            if response.status_code != 200:
                self.error = ResponseErrorModel(
                    status_code=response.status_code,
                    content=response.text,
                    json_content=response.json()
                )
                return

            self._cached_response = response
            return self.clean(self._cached_response.json())

    def get_model(self, data: dict[str, Any] | Sequence[dict[str, Any]] | None) -> T | Sequence[T] | None:
        """Convert the raw data into the specified model(s).

        Args:
            data (dict[str, Any] | Sequence[dict[str, Any]] | None): The raw data to be converted.

        Returns:
            T | Sequence[T] | None: The converted model instance(s) or None if no model is specified.
        """
        if data is None:
            return None
        
        if self.model is not None:
            if isinstance(data, list):
                return [self.model(**item) for item in data]
            
            if isinstance(data, dict):
                return self.model(**data)
        return None


class FileDownloadMixin[T = Sequence[dict[str, Any]]]:
    async def create_file(self, data: T):
        filename = secrets.token_hex(16)
        timestamp = datetime.datetime.now(tz=datetime.UTC).timestamp()
        filepath = DATA_DIR.joinpath(f"lawyers__{filename}__{timestamp}")

        df = pandas.DataFrame(data) # pyright: ignore[reportArgumentType]
        df.to_parquet(filepath, index=False)
