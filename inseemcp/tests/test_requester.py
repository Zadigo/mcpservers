from backend.base import (
    MultiCriteriaSearchEstablishment,
    query,
)
from backend.models import MultiCriteriaSearchQuery
from backend.operators import And, KeyValuePair, LegalUnitEnum


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

    condition = And(
        KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='A'),
        KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='B')
    )

    await query(instance, condition=condition)
