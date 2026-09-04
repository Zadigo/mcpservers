import pytest

from backend.simple_requester import MultiCriteriaSearchModel, Requester, SearchModel


async def test_raises_error():
    instance = Requester()
    with pytest.raises(ValueError):
        await instance(MultiCriteriaSearchModel(q='something'), testing=True)


async def test_single_search():
    instance = Requester(single_search=True)
    response = await instance(SearchModel(), url_param='123556', testing=True)
    assert response['url'] == 'https://api.insee.fr/api-sirene/3.11/siren/123556'
