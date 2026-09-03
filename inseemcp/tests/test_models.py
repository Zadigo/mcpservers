from backend.models import AND, OR
from models.base import LegalUnitEnum


def test_and():
    model = AND(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='My Legal Unit')
    assert model.resolve() == 'nomUniteLegale:My Legal Unit'
    assert model.operator_name == 'and'


def test_or():
    model = OR(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='My Legal Unit')
    assert model.resolve() == 'nomUniteLegale:My Legal Unit'
    assert model.operator_name == 'or'
