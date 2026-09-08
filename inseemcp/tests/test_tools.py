# from components.tools.base import search_entreprises_by_activity_codes
import pytest

from components.tools.establishments import (
    search_establishments_name_startswith,
)
from components.tools.legal_units import (
    establishments_siren_not_start_by,
    get_legal_unit_name_startswith,
    get_legal_units_by_name_and_location,
    get_siren_startswith,
    legal_units_exact_search,
)
from components.tools.university import get_university_by_siren, get_university_by_siret

# class TestSearchLegalUnitsByActivityCodes:
#     async def test_no_values(self):
#         result = await search_entreprises_by_activity_codes()
#         assert result is not None

#     async def test_with_values(self):
#         result = await search_entreprises_by_activity_codes(activity_codes=["84.23Z", "86.21Z"])
#         assert result is not None

#     async def test_with_values_and_condition(self):
#         result = await search_entreprises_by_activity_codes(activity_codes=["84.23Z", "86.21Z"], inclusive=True)
#         assert result is not None


@pytest.mark.e2e
class TestGetSirenStartsWith:
    async def test_no_values(self):
        result = await get_siren_startswith(siren="")
        assert result is not None

    async def test_with_values(self):
        result = await get_siren_startswith(siren="OpenAI")
        assert result is not None


@pytest.mark.e2e
class TestGetLegalUnitNameStartsWith:
    async def test_get_legal_unit_name_startswith(self):
        result = await get_legal_unit_name_startswith(name="OpenAI")
        assert result is not None


@pytest.mark.e2e
class TestEstablishmentsSirenNotStartBy:
    async def test_no_values(self):
        result = await establishments_siren_not_start_by(siren=[])
        assert result is not None

    async def test_with_values(self):
        result = await establishments_siren_not_start_by(siren=["1", "2"])
        assert result is not None


@pytest.mark.e2e
class TestSearchEstablishmentsNameStartsWith:
    async def test_no_values(self):
        result = await search_establishments_name_startswith(name="")
        assert result is not None

    async def test_with_values(self):
        result = await search_establishments_name_startswith(name="Lecl")
        assert result is not None


@pytest.mark.e2e
class TestLegalUnitsExactSearch:
    async def test_no_values(self):
        result = await legal_units_exact_search(column_name="", value="")
        assert result is not None
    
    async def test_with_values(self):
        result = await legal_units_exact_search(column_name ="NOM_UNITE_LEGALE", value="OpenAI")
        assert result is not None


@pytest.mark.e2e
class TestLegalUnitsByName:
    async def test_no_values(self):
        result = await get_legal_units_by_name_and_location(name="")
        assert result is not None

    async def test_with_values(self):
        result = await get_legal_units_by_name_and_location(name="Leclerc")
        assert result is not None

    async def test_with_values_and_postal_code(self):
        result = await get_legal_units_by_name_and_location(name="Leclerc", postal_code="5900")
        assert result is not None


@pytest.mark.e2e
class TestGetUniversityBySiren:
    async def test_no_values(self):
        result = await get_university_by_siren(siren="")
        assert result is not None

    async def test_with_values(self):
        result = await get_university_by_siren(siren="123456789")
        assert result is not None


@pytest.mark.e2e
class TestGetUniversityBySiret:
    async def test_no_values(self):
        result = await get_university_by_siret(siret="")
        assert result is not None

    async def test_with_values(self):
        result = await get_university_by_siret(siret="12345678901234")
        assert result is not None
