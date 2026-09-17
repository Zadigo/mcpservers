import json

import aiofile
import httpx2
import pytest

from backend.base import UniversityRequest
from models.university import UniversityModel
from utils import BASE_DIR


async def test_university_request():
    instance = UniversityRequest()
    await instance()
    assert instance._cached_response is not None
    assert instance._cached_response.status_code == 200


async def test_university_models():
    async with aiofile.async_open(BASE_DIR.joinpath('tests', 'example_universities.json')) as f:
        _data = await f.read()
        data = json.loads(_data)
        data = UniversityModel(**data[0])


@pytest.mark.e2e
async def test_university_():
    async with httpx2.AsyncClient() as client:
        response = await client.get('https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-principaux-etablissements-enseignement-superieur/exports/json')
        models = [UniversityModel(**item) for item in response.json()]
        assert len(models) > 0
