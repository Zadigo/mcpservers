import json

import aiofiles
import pytest

from utils import BASE_DIR


@pytest.fixture
async def mockresponse():
    json_file = BASE_DIR / 'tests' / 'example_response.json'
    async with aiofiles.open(json_file, mode='r') as f:
        str_json = await f.read()
        content = json.loads(str_json)
    return content
