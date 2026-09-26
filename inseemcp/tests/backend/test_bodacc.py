import pytest

from backend.base import BodaccRequest
from models.queries import BodaccQuery


@pytest.mark.e2e
async def test_bodacc_request():
    instance = BodaccRequest()
    response = await instance(query=BodaccQuery(where='824644587 in registre'))
    model = instance.get_model(response)
    assert instance.error is None
    assert model is not None


@pytest.mark.e2e
async def test_bodacc_request_fails():
    pass
