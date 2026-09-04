import os
from abc import ABC, abstractmethod
from typing import Any, Literal
from urllib.parse import urlencode

import httpx2

from backend.models import MultiCriteriaSearchQuery, SingleSearchQuery
from backend.typings import TypeCondition


class BaseRequest(ABC):
    version: float = 3.11
    param: Literal['siret', 'siren'] = 'siret'
    base_url: str = 'https://api.insee.fr/api-sirene/{version}/{param}'
    authorization_header: str = 'X-INSEE-Api-Key-Integration'

    def __init__(self):
        self._query_model: SingleSearchQuery | MultiCriteriaSearchQuery | None = None
        # self.q_condition: TypeCondition | None = None
        self.api_key: str = os.environ.get('INSEE_API_KEY')
        self.url_extra_params: dict = {}
        self._final_url: str | None = None

    def __repr__(self):
        return f'<{self.__class__.__name__}: query={self._query_model}>'

    @abstractmethod
    def get_url(self):
        """Returns the formatted base url built dynamically 
        using the version, param, and any extra url parameters"""
        url = self.base_url.format(version=self.version, param=self.param, **self.url_extra_params)

        if self._query_model is None:
            raise TypeError('The model used to set the query is not set')

        if isinstance(self._query_model, MultiCriteriaSearchQuery) and not isinstance(self._query_model.q, str):
            self._query_model.q = self._query_model.q.resolve()

        query = self._query_model.model_dump(exclude=['siren_ou_siret'], exclude_none=True)

        self._final_url = url
        
        if query:
            self._final_url = url + '?' + urlencode(query)
        return self._final_url

    def add_conditional_param(self, operator: TypeCondition):
        self.q_condition = operator
    
    async def send_request(self, url: str, testing: bool = False):
        """Sends a request to the Api using the paramters that
        were added in the url parameters"""
        if testing:
            return {'url': url, 'headers': {self.authorization_header: self.api_key}}
        
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            self.authorization_header: self.api_key
        }

        if self.api_key is None:
            raise ValueError('INSEE_API_KEY environment variable is not set')

        async with httpx2.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()


class SearchLegalUnitRequest(BaseRequest):
    """Request class responsible for sending a request to the Api for a legal unit"""

    param ='siren'
    base_url: str = 'https://api.insee.fr/api-sirene/{version}/{param}/{siren}'
    
    def get_url(self, **kwargs: Any):
       return super().get_url()


class SearchEstablishmentRequest(SearchLegalUnitRequest):
    """Request class responsible for sending a request to the Api
    for a single search of an establishment"""

    param = 'siret'
    base_url: str = 'https://api.insee.fr/api-sirene/{version}/{param}/{siret}'


class MultiCriteriaLegalUnitSearchRequest(BaseRequest):
    """Request class responsible for sending a request to the Api using multiple
    criteria for a legal unit search"""

    param = 'siren'

    def get_url(self, **kwargs: Any):
       return super().get_url()

    
class MultiCriteriaEstablishmentSearchRequest(MultiCriteriaLegalUnitSearchRequest):
    """Request class responsible for sending a request to the Api using multiple
    criteria for an establishment search"""

    param = 'siret'
    