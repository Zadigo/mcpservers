import pytest

from backend import (
    MultiCriteriaSearchEstablishment,
    SearchEstablishment,
    query,
)
from backend.models import MultiCriteriaSearchQuery, SingleSearchQuery
from backend.operators import And, KeyValuePair, LegalUnitEnum


class TestSingleSearchEstablishment:
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

        instance = MultiCriteriaSearchEstablishment(condition=condition)
        await query(instance, testing=True)
