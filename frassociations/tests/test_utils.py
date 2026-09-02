from utils import FilesQueryset


def test_iter_load_files_queryset():
    instance = FilesQueryset()
    files = list(instance)

    assert isinstance(files, list)
    assert len(files) > 0


async def test_prefetch_files():
    instance = FilesQueryset()
    df = await instance.prefetch_files(limit=2)

    assert df is not None
    assert not df.empty
