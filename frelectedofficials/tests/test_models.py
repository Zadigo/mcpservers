import pathlib

import pandas

from models.base import FileInfo

TEST_DIR = pathlib.Path(__file__).parent

def test_file_info(tmp_path):
    path = tmp_path.joinpath('test_file.csv')
    path.write_text('name,age\nAlice,30\nBob,25', encoding='utf-8')

    instance = FileInfo(
        title="Test Dataset", 
        filepath=str(path),
        using="DistrictCouncillor",
        created_on="2024-06-01"
    )

    assert instance.title == "Test Dataset"
    assert isinstance(instance.filename, str)
    assert isinstance(instance.get_content(), pandas.DataFrame)




# def test_get_content_as_model(tmp_path):
#     instance = FileInfo(
#         title='Test Dataset',
#         filename='elus-conseiller-darrondissement-ca.csv',
#         filepath='/elus-conseiller-darrondissement-ca.csv',
#         created_on='2024-06-01'
#     )
#     instance.get_content_as_model(DistrictCouncillorEN)
