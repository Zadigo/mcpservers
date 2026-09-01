import json
from functools import lru_cache

import pydantic

from utils import MEDIA_DIR, REGISTRY


class FileInfo(pydantic.BaseModel):
    title: str
    filepath: str
    created_on: str


class RegistryInfo(pydantic.BaseModel):
    count: int
    files: list[FileInfo]

    @property
    def filenames(self):
        return [item.title for item in self.files]

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


@lru_cache(maxsize=1)
def get_registry() -> RegistryInfo:
    with REGISTRY.open('r') as f:
        return RegistryInfo(**json.load(f))
