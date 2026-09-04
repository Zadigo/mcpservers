from unittest.mock import MagicMock, patch

import pytest

from backend import (
    MultiCriteriaSearchEstablishment,
    SearchEstablishment,
    query,
)
from backend.base import MultiCriteriaSearchLegalUnit, SearchLegalUnit
from backend.models import MultiCriteriaSearchQuery, SingleSearchQuery
from backend.operators import And, KeyValuePair, LegalUnitEnum
from backend.requests import (
    MultiCriteriaEstablishmentSearchRequest,
    MultiCriteriaLegalUnitSearchRequest,
    SearchEstablishmentRequest,
    SearchLegalUnitRequest,
)


class TestSearchEstablishment:
    async def test_invalid_request_builder(self):
        instance = SearchEstablishment()
        assert instance.query is not None
        assert instance.request is None

        with pytest.raises(ValueError):
            await query(instance, testing=True)

    async def test_valid_request_builder(self):
        instance = SearchEstablishment(SingleSearchQuery(siren_ou_siret='1234'))
        assert instance.query is not None
        assert instance.request is None

        response = await query(instance, testing=True)
        assert isinstance(response, dict)
        assert 'url' in response

        url = response['url']
        assert url == 'https://api.insee.fr/api-sirene/3.11/siret/1234'


class TestSearchLegalUnit:
    async def test_invalid_request_builder(self):
        instance = SearchLegalUnit(SingleSearchQuery(siren_ou_siret='1234'))
        response = await query(instance, testing=True)
        assert 'url' in response

        url = response['url']
        assert url == 'https://api.insee.fr/api-sirene/3.11/siren/1234'

    async def test_valid_request_builder(self):
        instance = SearchLegalUnit(SingleSearchQuery(siren_ou_siret='1234', date='2000-03-14'))
        response = await query(instance, testing=True)
        assert 'url' in response

        url = response['url']
        assert url == 'https://api.insee.fr/api-sirene/3.11/siren/1234?date=2000-03-14'


class TestMultiCriteriaSearchEstablishment:
    async def test_request_builder(self):
        instance = MultiCriteriaSearchEstablishment()
        response = await query(instance, testing=True)
        assert isinstance(response, dict)
        assert 'url' in response

        url = response['url']
        assert url == 'https://api.insee.fr/api-sirene/3.11/siret?q=&nombre=20'

    async def test_valid_request_builder(self):
        instance = MultiCriteriaSearchEstablishment(MultiCriteriaSearchQuery(q='some value'))
        response = await query(instance, testing=True)

        assert isinstance(response, dict)
        assert 'url' in response

        url = response['url']
        assert url == 'https://api.insee.fr/api-sirene/3.11/siret?q=some+value&nombre=20'


    async def test_request_builder_with_and(self):
        condition = And(
            KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='A'),
            KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='B')
        )

        q = MultiCriteriaSearchQuery(q=condition)
        instance = MultiCriteriaSearchLegalUnit(query=q)
        await query(instance, testing=True)

        assert instance.request._final_url == 'https://api.insee.fr/api-sirene/3.11/siren?q=nomUniteLegale%3AA+AND+nomUniteLegale%3AB&nombre=20'


class TestAbstractRequester:
    def test_instance(self):
        instance = SearchLegalUnit()
        assert instance.query is not None
        assert isinstance(instance.query, SingleSearchQuery)
        assert instance.request is None
        assert instance.condition is None

        instance = MultiCriteriaSearchLegalUnit()
        assert isinstance(instance.query, MultiCriteriaSearchQuery)

    def test_instance_with_wrong_query(self):
        with pytest.raises(TypeError):
            MultiCriteriaSearchLegalUnit(SingleSearchQuery())

    def test_request_builder(self):
        with patch.object(SearchLegalUnit, 'update_request_query'):
            instance = SearchLegalUnit()
            instance.request_builder()
            assert instance.request is not None

    def test_update_request_quer_no_request(self):
        with pytest.raises(ValueError):
            instance = SearchLegalUnit()
            instance.update_request_query()

    def test_udpate_request_with_request_and_query_empty(self):
        instance = SearchLegalUnit()
        instance.request = MagicMock(
            spec=SearchLegalUnitRequest,
            url_extra_params = {},
            _query_model=MagicMock()
        )

        with pytest.raises(ValueError):
            instance.update_request_query()

    def test_udpate_request_with_request_and_query(self):
        instance = SearchLegalUnit()
        instance.query.siren_ou_siret = 'some-query'

        expected_query_params = {'test-param': 'some-query', 'date': None}
        instance.request = MagicMock(
            param='test-param',
            spec=SearchLegalUnitRequest,
            url_extra_params = {},
            _query_model = MagicMock(model_copy=lambda update: update)
        )
        
        instance.update_request_query()
        assert instance.request._query_model == expected_query_params


@pytest.mark.parametrize(
    'testcase,klass',
    [
        ('siren', SearchLegalUnitRequest),
        ('siret', SearchEstablishmentRequest),
        ('siren - multi', MultiCriteriaLegalUnitSearchRequest),
        ('siret - multi', MultiCriteriaEstablishmentSearchRequest)
    ]
)
def test_base_request(testcase, klass):
    if 'siren' in testcase:
        assert klass.param == 'siren'
    else:
        assert klass.param == 'siret'

    assert klass.base_url is not None
    assert klass.base_url.startswith('https://api.insee.fr/api-sirene')


def test_multi_criteria_get_url_method_without_condition_no_model():
    instance = MultiCriteriaLegalUnitSearchRequest()
    instance._query_model = MagicMock(
        q = None,
        model_dump = lambda exclude_none: {'test': 'value'}
    )
    instance.q_condition = And(
        KeyValuePair(
            key=LegalUnitEnum.CARACTERE_EMPLOYEUR_UNITE_LEGALE,
            value='some-value'
        ),
        KeyValuePair(
            key=LegalUnitEnum.CARACTERE_EMPLOYEUR_UNITE_LEGALE,
            value='some-value'
        )
    )
    with pytest.raises(TypeError):
        instance.get_url()
