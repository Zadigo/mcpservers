from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any, Literal
from urllib.parse import urlencode

from backend.models import (
    AND,
    OR,
    MultiCriteriaSearchQuery,
    SingleSearchQuery,
    StartsWithQuery,
)


class AbstractRequester(ABC):
    def __init__(self, query: SingleSearchQuery | MultiCriteriaSearchQuery = None):
        self.query = query
        self.request: BaseRequest | None = None

    @abstractmethod
    def request_builder(self, using: BaseRequest | None = None) -> BaseRequest:
        pass

    def update_request_query(self):
        query_data: dict = {}
        if self.query is not None:
            query_data = self.query.model_dump()

        new_values = self.request.query_params | query_data
        self.request.add_query_param_from_dict(new_values)
        

class SingleSearchLegalUnit(AbstractRequester):
    def __init__(self, query: SingleSearchQuery = None):
        super().__init__(query)

    def request_builder(self):
        self.request = SingleSearchLegalUnitRequest()
        self.update_request_query()
        return self.request


class SingleSearchEstablishment(AbstractRequester):
    def request_builder(self):
        self.request = SingleSearchEstablishmentRequest()
        self.update_request_query()
        return self.request


class MultiCriteriaSearchMixin(AbstractRequester):
    def __init__(self, query: MultiCriteriaSearchQuery = None):
        super().__init__(query)

    def starts_with(self, query: str | StartsWithQuery):
        if isinstance(query, str):
            query = StartsWithQuery(q=query)

        data = query.model_dump()
        for key, value in data.items():
            self.request.add_query_param(key, value)

        return self

    def between(self, query: StartsWithQuery):
        return self

    def conditional_and(self, *query: AND):
        return self

    def conditional_or(self, *query: OR):
        return self


class MultiCriteriaSearchLegalUnit(MultiCriteriaSearchMixin):
    def request_builder(self):
        self.request = MultiCriteriaLegalUnitSearchRequest()
        self.update_request_query()
        return self.request


class MultiCriteriaSearchEstablishment(MultiCriteriaSearchMixin):
    """Entrypoint for a sending a multi-criteria search to the Api"""
    
    def request_builder(self):
        self.request = MultiCriteriaEstablishmentSearchRequest()
        self.update_request_query()
        return self.request


class BaseRequest(ABC):
    version: float = 3.11
    param: Literal['siret', 'siren'] = 'siret'
    base_url: str = 'https://api.insee.fr/api-sirene/{version}/{param}'

    def __init__(self):
        self.query_params: dict[str, str] = {}
        self.conditional_params: Sequence[AND | OR] = []

    @abstractmethod
    def get_url(self, **kwargs: Any):
        return self.base_url.format(version=self.version, param=self.param, **kwargs)

    def add_query_param_from_dict(self, values: dict, ignore_empty: bool = False):
        for key, value in values.items():
            self.add_query_param(key, value, ignore_empty=ignore_empty)
    
    def add_query_param(self, key: str, value: str | None, ignore_empty: bool = False):
        """Add url params to the request dictionnary by ignoring nullish values"""
        if value is None:
            value = ''

        if ignore_empty:
            return
        
        if key in self.query_params:
            self.query_params.update(**{key: value})
        else:
            self.query_params[key] = value

    def add_conditional_param(self, operator: AND | OR):
        self.conditional_params.append(operator)
    
    async def send_request(self, url: str):
        """Sends a request to the Api using the paramters that
        were added in the url parameters"""
        print(f'sending request using the url: {url}')

        # async with httpx2.AsyncClient() as client:
        #     response = await client.get(url)
        #     response.raise_for_status()
        #     return response.json()


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

        if self.query_params:
            url = url + '?' + urlencode(self.query_params)

        return url

    
class MultiCriteriaEstablishmentSearchRequest(MultiCriteriaLegalUnitSearchRequest):
    param = 'siret'
    

async def query(requester: AbstractRequester, **kwargs: Any) -> dict[str, Any]:
    instance = requester.request_builder()
    return await instance.send_request(instance.get_url(**kwargs))
