
from models.base import (
    BaseResponseModel,
)


async def test_base_response_model_validation(mockresponse):
    model = BaseResponseModel(**mockresponse)
    assert model.etablissements[0].siren == '775672272'
