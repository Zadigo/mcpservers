import pytest

from backend.operators import (
    And,
    KeyValuePair,
    LegalUnitEnum,
    Or,
    Period,
    WildCard,
)


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



def test_key_value_pair():
    kv = KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value=None)
    assert kv.resolve() == 'nomUniteLegale:'


@pytest.mark.parametrize(
    'name,expected,key_value',
    [
        ('not inverted', 'nomUniteLegale:test*', KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='test')),
        ('inverted with value', '-nomUniteLegale:test*', KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='test')),
        ('inverted with None', '-nomUniteLegale:*', KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value=None)),
    ]
)
def test_wildcard_not_inverted(name, expected, key_value):
    wc = WildCard(key_value)
    if name.startswith('inverted'):
        result = ~wc
    else:
        result = wc.resolve()

    assert isinstance(result, (KeyValuePair, str))
    if isinstance(result, KeyValuePair):
        assert result.resolve() == expected
    else:
        assert result == expected


def test_wildcard_inverted_and():
    logic_and = And(
        ~WildCard(KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='test')),
        ~WildCard(KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='test'))
    )

    assert logic_and.resolve() == '-nomUniteLegale:test* AND -nomUniteLegale:test*'



def test_period():
    instance = Period(
        Or(
            KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='A'),
            KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='B')
        )
    )
    assert instance.resolve() == 'periode(nomUniteLegale:A OR nomUniteLegale:B)'
