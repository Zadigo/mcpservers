from backend.base import (
    MultiCriteriaSearchEstablishment,
    query,
)
from backend.models import AND, LegalUnitEnum, MultiCriteriaSearchQuery


async def test_starts_with():
    pass
    # instance = SingleSearchEstablishment()
    # instance.starts_with()
    # query(instance)


async def test_request_builder():
    instance = MultiCriteriaSearchEstablishment()
    await query(instance)


async def test_request_builder_with_query():
    instance = MultiCriteriaSearchEstablishment(MultiCriteriaSearchQuery(q='some value'))
    await query(instance)


async def test_request_builder_with_and():
    instance = MultiCriteriaSearchEstablishment()

    and1 = AND(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='My Legal Unit')
    and2 = AND(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='Another Legal Unit')

    instance.conditional_and(and1, and2)
    await query(instance)
