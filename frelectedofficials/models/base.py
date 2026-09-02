import io
import json
import pathlib
from functools import lru_cache

import pandas
import pydantic

from utils import MEDIA_DIR, REGISTRY, redis_client


class FileInfo(pydantic.BaseModel):
    title: str
    filepath: str
    created_on: str

    @property
    def filename(self):
        return pathlib.Path(self.filepath).name

    def get_content(self, as_json: bool = False) -> pandas.DataFrame | list[dict]:
        client = redis_client()
        data = client.get(f'{self.filename}:data')

        if data is not None:
            df = pandas.read_csv(io.StringIO(data), sep=';')
            if as_json:
                return json.loads(df.to_json(orient='records'))
            return df
        
        with open(self.filepath, 'r', encoding='utf-8') as f:
            df = pandas.read_csv(f, encoding='utf-8')
            client.set(f'{self.filename}:data', df.to_csv(index=False))

            if as_json:
                return json.loads(df.to_json(orient='records'))

            return df

    def get_content_as_model[T = pydantic.BaseModel](self, model: type[T]) -> list[T]:
        df = self.get_content()
        return [model(**row) for row in json.loads(df.to_json(orient='records'))]


class RegistryInfo(pydantic.BaseModel):
    count: int
    files: list[FileInfo]

    @property
    def filetitles(self):
        return [item.title for item in self.files]

    @property
    def str_filetitles(self):
        return ', '.join(self.filetitles)

    async def create_file(self):
        fullpath = MEDIA_DIR / 'registry.json'
        with fullpath.open('w', encoding='utf-8') as f:
            f.write(self.model_dump_json(indent=2, ensure_ascii=False))

    def add_file(self, file_info: FileInfo):
        self.count += 1
        self.files.append(file_info)

    def get_file_by_title(self, title: str) -> FileInfo | None:
        for file_info in self.files:
            if file_info.title == title:
                return file_info
        return None


class GroupingByGender(pydantic.BaseModel):
    F: int = 0
    H: int = 0


class GroupingByJobCategory(pydantic.BaseModel):
    job_name: str = ''
    count: int = 0


@lru_cache(maxsize=1)
def get_registry() -> RegistryInfo:
    with REGISTRY.open('r') as f:
        return RegistryInfo(**json.load(f))
