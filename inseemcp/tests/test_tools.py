from components.tools.base import search_entreprises_by_activity_codes
from components.tools.establishments import (
    establishments_siren_not_start_by,
    search_establishments_name_startswith,
)
from components.tools.legal_units import (
    get_legal_unit_name_startswith,
    get_siren_startswith,
    legal_units_column_has_no_value,
    legal_units_exact_search,
)


class TestSearchLegalUnitsByActivityCodes:
    async def test_no_values(self):
        result = await search_entreprises_by_activity_codes()
        assert result is not None

    async def test_with_values(self):
        result = await search_entreprises_by_activity_codes(activity_codes=["84.23Z", "86.21Z"])
        assert result is not None

    async def test_with_values_and_condition(self):
        result = await search_entreprises_by_activity_codes(activity_codes=["84.23Z", "86.21Z"], inclusive=True)
        assert result is not None



class TestGetSirenStartsWith:
    async def test_no_values(self):
        result = await get_siren_startswith(name="")
        assert result is not None

    async def test_with_values(self):
        result = await get_siren_startswith(name="OpenAI")
        assert result is not None


class TestGetLegalUnitNameStartsWith:
    async def test_get_legal_unit_name_startswith(self):
        result = await get_legal_unit_name_startswith(name="OpenAI")
        assert result is not None

    async def test_legal_units_column_has_no_value(self):
        result = await legal_units_column_has_no_value(siren="123456789", column="NOM_UNITE_LEGALE")
        assert result is not None



class TestEstablishmentsSirenNotStartBy:
    async def test_no_values(self):
        result = await establishments_siren_not_start_by(siren=[])
        assert result is not None

    async def test_with_values(self):
        result = await establishments_siren_not_start_by(siren=["1", "2"])
        assert result is not None



class TestSearchEstablishmentsNameStartsWith:
    async def test_no_values(self):
        result = await search_establishments_name_startswith(name="")
        assert result is not None

    async def test_with_values(self):
        result = await search_establishments_name_startswith(name="OpenAI")
        assert result is not None



class TestLegalUnitsExactSearch:
    async def test_no_values(self):
        result = await legal_units_exact_search(column="", value="")
        assert result is not None

    async def test_with_values(self):
        result = await legal_units_exact_search(column="NOM_UNITE_LEGALE", value="OpenAI")
        assert result is not None
