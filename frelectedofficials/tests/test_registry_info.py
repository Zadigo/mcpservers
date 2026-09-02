import datetime

import pytest

from models.base import FileInfo, RegistryInfo

d = datetime.datetime.now(tz=datetime.UTC).date()

@pytest.fixture
def registry():
    return RegistryInfo(count=0, files=[])


@pytest.mark.parametrize(
    'name,data',
    [
        ('File A', {'title': 'File A', 'filepath': '/path/a', 'using': 'A', 'created_on': str(d)}),
        ('File B', {'title': 'File B', 'filepath': '/path/a', 'using': 'A', 'created_on': str(d)}),
        ('File C', {'title': 'File C', 'filepath': '/path/a', 'using': 'A', 'created_on': str(d)}),
    ]
)
async def test_file_creation_multiple(registry, name, data):
    fileinfo = FileInfo(**data)
    registry.add_file(fileinfo)
    print(registry.count)
    # assert registry.count >= 0

    # await registry.create_file()
