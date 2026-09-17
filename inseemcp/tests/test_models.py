import json

import aiofiles

from models.lawyers import LawyersModel
from models.university import UniversityModel
from utils import BASE_DIR


async def test_university_models():
    async with aiofiles.open(BASE_DIR.joinpath('tests', 'example_universities.json')) as f:
        _data = await f.read()

        data = json.loads(_data)
        data = UniversityModel(**data[0])

        assert data is not None
        assert isinstance(data, UniversityModel)


async def test_lawyers_model(mocked_lawyers):
    data = LawyersModel(**mocked_lawyers[0])

    assert data is not None
    assert isinstance(data, LawyersModel)
