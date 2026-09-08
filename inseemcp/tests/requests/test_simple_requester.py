import pytest

from backend.simple_requester import (
    MultiCriteriaSearchModel,
    SearchModel,
    condition_and,
    condition_or,
    condition_period,
    condition_to,
    inversion,
    key_value_pair,
    wild_card,
)
from models.base import BusinessColumnEnum


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


def test_condition_period():
    assert condition_period("someYear:2025") == "periode(someYear:2025)"


def test_condition_to():
    assert condition_to("someYear:2025", "someYear:2026") == "[someYear:2025 TO someYear:2026]"


def test_condition_or():
    assert condition_or(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, "value1", "value2") == "denominationUniteLegale:value1 OR denominationUniteLegale:value2"


def test_condition_and():
    assert condition_and(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, "value1", "value2") == "denominationUniteLegale:value1 AND denominationUniteLegale:value2"


def test_key_value_pair():
    assert key_value_pair(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, "value") == "denominationUniteLegale:value"


@pytest.mark.parametrize(
    'input,expected',
    [
        ("value*", "denominationUniteLegale:value*"),
        ("value", "denominationUniteLegale:value*"),
    ]
)
def test_wild_card(input, expected):
    assert wild_card(BusinessColumnEnum.DENOMINATION_UNITE_LEGALE, input) == expected


def test_inversion():
    assert inversion("value") == "-value"
