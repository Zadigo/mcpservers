import os
from abc import ABC, abstractmethod
from typing import Any, Literal
from urllib.parse import urlencode

import httpx2

from backend.models import MultiCriteriaSearchQuery, SingleSearchQuery
from backend.operators import And, Or, Period, To

type TypeCondition = And | To | Period


class AbstractRequester(ABC):
    def __init__(self, query: SingleSearchQuery | MultiCriteriaSearchQuery = None):
        self.query = query
        self.request: BaseRequest | None = None

    @abstractmethod
    def request_builder(self, using: BaseRequest | None = None, condition: TypeCondition | None = None) -> BaseRequest:
        """Builds the BaseRequest class that will responsible for sending request"""

    def update_request_query(self):
        model = getattr(self.request, '_query_model', None)
        if model is None:
            self.request._query_model = self.query
        else:
            if self.query is not None:
                data = self.query.model_dump()
                for key, value in data.items():
                    self.request._query_model[key] = value
    

class SingleSearchLegalUnit(AbstractRequester):
    def __init__(self, query: SingleSearchQuery = None):
        if query is None:
            query = SingleSearchQuery()
        else:
            if not isinstance(query, SingleSearchQuery):
                raise ValueError('Query should be an instance of SingleSearchQuery')
            
        super().__init__(query)

    def request_builder(self, condition: TypeCondition | None = None):
        self.request = SingleSearchLegalUnitRequest()
        self.update_request_query()
        return self.request


class SingleSearchEstablishment(AbstractRequester):
    def request_builder(self, condition: TypeCondition | None = None):
        self.request = SingleSearchEstablishmentRequest()
        self.update_request_query()
        return self.request


class MultiCriteriaSearchMixin(AbstractRequester):
    def __init__(self, query: MultiCriteriaSearchQuery = None):
        if query is None:
            query = MultiCriteriaSearchQuery()
        else:
            if not isinstance(query, MultiCriteriaSearchQuery):
                raise ValueError('Query should be an instance of MultiCriteriaSearchQuery')

        super().__init__(query)


class MultiCriteriaSearchLegalUnit(MultiCriteriaSearchMixin):
    def request_builder(self, condition: TypeCondition | None = None):
        self.request = MultiCriteriaLegalUnitSearchRequest()
        self.request.q_condition = condition
        self.update_request_query()
        return self.request


class MultiCriteriaSearchEstablishment(MultiCriteriaSearchMixin):
    """Entrypoint for a sending a multi-criteria search to the Api"""

    def request_builder(self, condition: TypeCondition | None = None):
        self.request = MultiCriteriaEstablishmentSearchRequest()
        self.request.q_condition = condition
        self.update_request_query()
        return self.request


class BaseRequest(ABC):
    version: float = 3.11
    param: Literal['siret', 'siren'] = 'siret'
    base_url: str = 'https://api.insee.fr/api-sirene/{version}/{param}'
    authoriazation_header:str = 'X-INSEE-Api-Key-Integration'

    def __init__(self):
        self._query_model: SingleSearchQuery | MultiCriteriaSearchQuery | None = None
        self.q_condition: And | Or | Period = None
        self.api_key: str = os.environ.get('INSEE_API_KEY')

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.param}>'

    @abstractmethod
    def get_url(self):
        """Returns the formatted base url used for the Api request"""
        return self.base_url.format(version=self.version, param=self.param)

    def add_conditional_param(self, operator: And | Or | Period | To):
        self.q_condition = operator
    
    async def send_request(self, url: str):
        """Sends a request to the Api using the paramters that
        were added in the url parameters"""
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            self.authoriazation_header: self.api_key
        }

        if self.api_key is None:
            raise ValueError('INSEE_API_KEY environment variable is not set')

        async with httpx2.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()


class SingleSearchLegalUnitRequest(BaseRequest):
    param ='siren'
    
    def get_url(self, **kwargs: Any):
       return super().get_url(**kwargs)


class SingleSearchEstablishmentRequest(SingleSearchLegalUnitRequest):
    param = 'siret'


class MultiCriteriaLegalUnitSearchRequest(BaseRequest):
    param = 'siren'

    def get_url(self, **kwargs: Any):
        url = super().get_url(**kwargs)

        if self.q_condition is not None:
            self._query_model.q = self.q_condition.resolve()

        return url + '?' + urlencode(self._query_model.model_dump())

    
class MultiCriteriaEstablishmentSearchRequest(MultiCriteriaLegalUnitSearchRequest):
    param = 'siret'
    

async def query(requester: AbstractRequester, condition: And | Or | To | Period | None = None) -> dict[str, Any]:
    instance = requester.request_builder(condition=condition)
    return await instance.send_request(instance.get_url())
