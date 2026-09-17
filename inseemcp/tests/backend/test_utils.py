from unittest.mock import AsyncMock, Mock, patch

import httpx2
import pytest

from backend.base import UniversityRequest
from backend.utils import BaseRequest
from models.university import UniversityModel


class SimpleRequest(BaseRequest):
    pass


def test_base_request_instance():
    instance = SimpleRequest()
    assert isinstance(instance, BaseRequest)


async def test_base_request_no_url():
    with pytest.raises(ValueError):
        instance = SimpleRequest()
        await instance()


@pytest.mark.parametrize(
    "status_code",
    [
        200,
        404,
        500
    ]
)
async def test_simple_request_instance_call(status_code):
    if status_code == 200:
        expected_value = [{"id": 1, "title": "Test Todo"}]
    else:
        expected_value = {'error': 'some error occured'}

    with patch('backend.utils.httpx2.AsyncClient') as mclient:
        mock_response = Mock(
            status_code=status_code,
            json=Mock(return_value=expected_value),
            text=str(expected_value)
        )
        mclient.get = AsyncMock(return_value=mock_response)
        mclient.return_value.__aenter__.return_value = mclient
        mclient.return_value.__aexit__.return_value = None

        instance = SimpleRequest()
        instance.base_url = 'https://jsonplaceholder.typicode.com/todos/'
        value = await instance()

        if status_code == 200:
            assert value == expected_value
            assert instance.dataframe is not None
            assert not instance.dataframe.empty
        else:
            assert instance.error is not None
            assert instance._cached_response is None
            assert instance.error.status_code == status_code
            assert value is None


@pytest.mark.e2e
class TestUniversityRequest:
    async def test_results(self):
        instance = UniversityRequest()

        await instance()

        assert instance._cached_response is not None
        assert instance._cached_response.status_code == 200

    async def test_endpoint(self):
        async with httpx2.AsyncClient() as client:
            response = await client.get('https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-principaux-etablissements-enseignement-superieur/exports/json')
            models = [UniversityModel(**item) for item in response.json()]
            assert len(models) > 0
