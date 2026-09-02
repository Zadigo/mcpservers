import asyncio
import inspect
import json
import pathlib
from functools import lru_cache
from importlib import import_module

import pandas
import pydantic

from utils import MEDIA_DIR, REGISTRY


class FileInfo(pydantic.BaseModel):
    """Represents information about a file in the registry.
    
    Attributes:
        title (str): The title of the file.
        filepath (str): The path to the file.
        using (str): The class factory that created the file.
        created_on (str): The creation timestamp of the file.
    """

    title: str
    filepath: str
    using: str
    created_on: str

    @property
    def filename(self):
        return pathlib.Path(self.filepath).name

    def get_content(self, as_json: bool = False) -> pandas.DataFrame | list[dict]:
        from endpoints.factories import ElectedOfficials

        try: 
            module = import_module('endpoints.factories')
        except ModuleNotFoundError:
            raise RuntimeError("The 'endpoints.factories' module is not found. Ensure that the module exists and is accessible.")
        else:
            candidates: list[type[ElectedOfficials]] = [
                klass for name, klass in inspect.getmembers(module, inspect.isclass)
                if name == self.using and issubclass(klass, ElectedOfficials)
            ]

            if candidates:
                klass = candidates[0]
                instance = klass()
                return asyncio.run(instance.get_dataframe())
            
            raise RuntimeError("No suitable ElectedOfficials class found in 'endpoints.factories' module.")


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
    # TODO: Register the registry in redis
    with REGISTRY.open('r') as f:
        return RegistryInfo(**json.load(f))
