from abc import ABC, abstractmethod
from typing import Final

from backend.models import MultiCriteriaSearchQuery, SingleSearchQuery
from backend.requests import (
    MultiCriteriaEstablishmentSearchRequest,
    MultiCriteriaLegalUnitSearchRequest,
    SearchEstablishmentRequest,
    SearchLegalUnitRequest,
)
from backend.typings import TypeBaseRequest


class AbstractRequester(ABC):
    """Base factory class used to build a request to the Api.
    
    Aargs:
        query: SingleSearchQuery | MultiCriteriaSearchQuery = None
            The query model that will be used to build the request
        condition: TypeCondition | None = None
            The condition that will be used to build the request
    """

    is_multi_criteria: Final[bool] = False

    def __init__(self, query: SingleSearchQuery | MultiCriteriaSearchQuery = None):
        self.query = query
        self.request: TypeBaseRequest | None = None

        if query is None:
            if self.is_multi_criteria:
                self.query = MultiCriteriaSearchQuery()
            else:
                self.query = SingleSearchQuery(siren_ou_siret='')
        else:
            if self.is_multi_criteria and not isinstance(self.query, MultiCriteriaSearchQuery):
                raise TypeError("Expected a MultiCriteriaSearchQuery for a multi-criteria requester")

    @abstractmethod
    def request_builder(self, using: TypeBaseRequest | None = None) -> TypeBaseRequest:
        """Builds the BaseRequest class that will responsible for sending request

        Args:
            using: TypeBaseRequest | None = None
                The BaseRequest class that will be used to send the request. If None, the default BaseRequest class will be used
        """
        self.request = using
        self.update_request_query()

    def update_request_query(self):
        if self.request is None:
            raise ValueError('Cannot update a request that is None')
        
        model = getattr(self.request, '_query_model', None)
        if model is None:
            self.request._query_model = self.query

        if not self.is_multi_criteria:
            if self.query.siren_ou_siret == '':
                raise ValueError('Trying to call a SearchLegalUnitRequest without a parameter will create a malformed url')
        
            self.request.url_extra_params[self.request.param] = self.query.siren_ou_siret        


class SearchLegalUnit(AbstractRequester):
    """Entrypoint for building a request that will return 
    information about a legal unit by using the SIREN number"""
    
    def request_builder(self):
        super().request_builder(using=SearchLegalUnitRequest())
        return self.request


class SearchEstablishment(AbstractRequester):
    """Entrypoint for building a request that will return
    information about an establishment by using the SIRET number"""

    def request_builder(self):
        super().request_builder(using=SearchEstablishmentRequest())
        return self.request


class MultiCriteriaSearchLegalUnit(AbstractRequester):
    """Entrypoint for building a request that will return
    information about a legal unit by using multiple criteria"""

    is_multi_criteria: Final[bool] = True

    def request_builder(self):
        super().request_builder(using=MultiCriteriaLegalUnitSearchRequest())
        return self.request


class MultiCriteriaSearchEstablishment(AbstractRequester):
    """Entrypoint for building a request that will return
    information about an establishment by using multiple criteria"""

    is_multi_criteria: Final[bool] = True

    def request_builder(self):
        super().request_builder(using=MultiCriteriaEstablishmentSearchRequest())
        return self.request


