import pytest

from components.tools.lawyers import FileQueryset


@pytest.fixture
def instance():
    return FileQueryset()


def test_file_queryset(instance):
    df = instance.load_cache()
    assert df is not None
    assert not df.empty


def test_get_by_siren(instance):
    siren = "988689832"
    results = instance.get_by_siren(siren)
    assert results is not None
    assert isinstance(results, list)
