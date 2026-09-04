import pytest

from backend.models import StrMultiSearchQuery
from backend.operators import KeyValuePair, LegalUnitEnum
from models.base import (
    BaseResponseModel,
)


@pytest.fixture
def keyvalue_one():
    return KeyValuePair(key=LegalUnitEnum.PRENOM3_UNITE_LEGALE, value='value1')


@pytest.fixture
def keyvalue_two():
    return KeyValuePair(key=LegalUnitEnum.PRENOM3_UNITE_LEGALE, value='value2')


async def test_base_response_model_validation(mockresponse):
    model = BaseResponseModel(**mockresponse)
    assert model.etablissements[0].siren == '775672272'



def test_str_multi_search_query_validation():
    model = StrMultiSearchQuery(q='Something')
    assert model.q == 'Something'


# def test_condition_multi_search_query_validation(keyvalue_one, keyvalue_two):
#     condition = And(lhv=keyvalue_one, rhv=keyvalue_two)
#     model = ConditionMultiSearchQuery(q=condition)
#     assert model.q == condition
