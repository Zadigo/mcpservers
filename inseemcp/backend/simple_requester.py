import os
from typing import Literal
from urllib.parse import urlencode

import httpx2
import pydantic
from pydantic import Field

from backend.models import ResponseErrorModel

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
        self.error: ResponseErrorModel | None = None
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
            # Handle different HTTP response status codes
            match response.status_code:
                case 500:
                    self.error = ResponseErrorModel(
                        status_code=500,
                        content=f"Internal server error: {response.content}",
                    )
                    return None

                case 404:
                    self.error = ResponseErrorModel(
                        status_code=404,
                        content="The requested resource was not found",
                        json_content=response.json()
                    )
                    return None

                case 200:
                    self._cached_response = response
                    return self._cached_response.json()

                case _:
                    self.error = ResponseErrorModel(
                        status_code=response.status_code,
                        content=f"Unexpected status code: {response.content}",
                    )
                    return None
