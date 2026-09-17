# from components.tools.base import search_entreprises_by_activity_codes
import pytest

from components.tools.establishments import (
    get_siret,
    search_establishments_by_code_naf,
    search_establishments_name_startswith,
)
from components.tools.university import get_university_by_siren, get_university_by_siret


@pytest.mark.e2e
class TestUniversityTools:
    async def test_get_university_by_siren(self):
        result = await get_university_by_siren(siren="824644587")
        assert result is not None

    async def test_get_university_by_siret(self):
        result = await get_university_by_siret(siret="82464458700027")
        assert result is not None


@pytest.mark.e2e
class TestEstablishmentsTools:
    async def test_get_siret(self):
        result = await get_siret(siret="82464458700027")
        assert result is not None

    async def test_search_establishments_name_startswith(self):
        result = await search_establishments_name_startswith(name="Insee")
        assert result is not None


    async def test_search_establishments_by_code_naf(self):
        result = await search_establishments_by_code_naf(code_naf="62.01Z")
        assert result is not None



@pytest.mark.e2e
class TestLegalUnits:
    def test_get_siren(self):
        pass


    async def test_search_legal_units_by_siren_prefix(self):
        pass

    async def test_search_legal_units_by_name_prefix(self):
        pass

    async def test_get_legal_units_column_has_no_value(self):
        pass

    async def test_get_legal_units_by_name_and_location(self):
        pass

    async def test_search_legal_units_by_address(self):
        pass
