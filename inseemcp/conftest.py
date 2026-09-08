import json
from unittest.mock import MagicMock, Mock, PropertyMock, patch

import aiofiles
import pytest

from backend.simple_requester import Requester
from utils import BASE_DIR


@pytest.fixture
def api_request():
    return Requester()


@pytest.fixture
async def mockresponse():
    json_file = BASE_DIR / 'tests' / 'example_response.json'
    async with aiofiles.open(json_file, mode='r') as f:
        str_json = await f.read()
        content = json.loads(str_json)
    return content


@pytest.fixture
def mocked_request():
    with patch('backend.simple_requester.httpx2') as mhttpx2:
        mhttpx2.AsyncClient.__enter__ = PropertyMock(
            get=Mock(
                response=Mock(
                    status_code=200,
                    json=[]
                )
            )
        )
        mhttpx2.AsyncClient.__aexit__ = PropertyMock()
        mock = MagicMock(
            spec=Requester,
            
        )
        return mock
