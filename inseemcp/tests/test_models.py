import pytest

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
