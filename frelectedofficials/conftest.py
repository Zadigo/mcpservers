import pytest

from endpoints.factories import ElectedOfficials
from models.base import FileInfo


@pytest.fixture
def elected_officials() -> ElectedOfficials:
    """
    Fixture to provide an instance of the ElectedOfficials class for testing.
    """
    class ElectedOfficialsMock(ElectedOfficials):
        url: str = 'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-154541/elus-conseiller-darrondissement-ca.csv'
        filename: str = 'test-elus-conseiller-darrondissement-ca.csv'
        fr_title: str = "Élus Conseiller d'Arrondissement"

        def get_dataframe(self):
            return super().get_dataframe()

    return ElectedOfficialsMock()



@pytest.fixture
def fileinfo(tmp_path) -> FileInfo:
    path = tmp_path.joinpath('test_file.csv')
    path.write_text('name,age\nAlice,30\nBob,25', encoding='utf-8')
    
    return FileInfo(
        title="Test Dataset", 
        filepath=str(tmp_path.joinpath('test_file.csv')),
        using="DistrictCouncillor",
        created_on="2024-06-01"
    )
