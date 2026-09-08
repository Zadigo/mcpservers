# from components.tools.base import search_entreprises_by_activity_codes
import pytest

from components.tools.establishments import (
    search_establishments_name_startswith,
)
from components.tools.legal_units import (
    get_legal_units_by_name_and_location,
    search_legal_units_by_name_prefix,
    search_legal_units_by_siren_prefix,
)
from components.tools.university import get_university_by_siren, get_university_by_siret


@pytest.mark.e2e
class TestGetSirenStartsWith:
    async def test_with_values(self):
        result = await search_legal_units_by_siren_prefix(siren_prefix="3")
        assert result is not None

    async def test_all_params(self):
        result = await search_legal_units_by_siren_prefix(
            siren_prefix="3",
            active_state="active",
            legal_unit_category="MIC",
            date="2024-01-01",
            offset=0
        )
        assert result is not None


@pytest.mark.e2e
class TestGetLegalUnitNameStartsWith:
    async def test_all_params(self):
        result = await search_legal_units_by_name_prefix(name_prefix="leclerc")
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
