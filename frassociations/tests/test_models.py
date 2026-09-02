import json

from models.results import AssociationModel
from utils import FilesQueryset


async def test_association_model():
    instance = FilesQueryset()
    df = await instance.prefetch_files()
    json_data = json.loads(df.to_json(orient="records"))

    for data in json_data:
        model = AssociationModel(**data)
        assert model.id is not None
