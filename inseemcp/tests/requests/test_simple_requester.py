import pytest

from backend.simple_requester import MultiCriteriaSearchModel, SearchModel


@pytest.mark.e2e
async def test_raises_error(api_request):
    with pytest.raises(ValueError):
        await api_request(MultiCriteriaSearchModel(q='something'), testing=True)


@pytest.mark.e2e
async def test_single_search(api_request):
    response = await api_request(SearchModel(), url_param='123556', testing=True)
    assert response['url'] == 'https://api.insee.fr/api-sirene/3.11/siren/123556'



async def test_simple_requester(api_request, mocked_request):
    response = await api_request(SearchModel())
    assert response is not None
