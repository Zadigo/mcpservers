from backend.operators import And, KeyValuePair, Or
from models.base import LegalUnitEnum


def test_and():
    model = And(
        KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='A'),
        KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='B')
    )
    assert model.resolve() == 'nomUniteLegale:A AND nomUniteLegale:B'


def test_or():
    model = Or(
        KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='A'),
        KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='B')
    )
    assert model.resolve() == 'nomUniteLegale:A OR nomUniteLegale:B'
