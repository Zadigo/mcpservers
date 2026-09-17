from unittest.mock import AsyncMock, Mock, patch

import pytest

from backend.utils import BaseRequest


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
