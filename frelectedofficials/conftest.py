import pytest

from endpoints.factories import ElectedOfficials


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
