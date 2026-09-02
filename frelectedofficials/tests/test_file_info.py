import pandas


def test_file_info_instance(fileinfo):
    assert fileinfo.title == "Test Dataset"
    assert isinstance(fileinfo.filename, str)


def test_get_content_as_json(fileinfo):
    content = fileinfo.get_content_as_json()
    assert isinstance(content, list)


def test_get_dataframe(fileinfo):
    df = fileinfo.get_content()
    assert isinstance(df, pandas.DataFrame)
    