from models.bodacc import BodaccModel
from models.lawyers import LawyersModel
from models.university import UniversityModel


async def test_university_models(json_universities):
    data = UniversityModel(**json_universities[0])
    assert data is not None
    assert isinstance(data, UniversityModel)


async def test_lawyers_model(mocked_lawyers):
    data = LawyersModel(**mocked_lawyers[0])

    assert data is not None
    assert isinstance(data, LawyersModel)


async def test_bodacc_model(json_bodacc):
    data = BodaccModel(**json_bodacc['results'][0])

    assert data is not None
    assert isinstance(data, BodaccModel)
