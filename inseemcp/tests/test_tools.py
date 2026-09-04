from components.tools.base import search_legal_units_by_activity_codes


class TestSearchLegalUnitsByActivityCodes:
    async def test_no_values(self):
        result = await search_legal_units_by_activity_codes()
        assert result is not None

    async def test_with_values(self):
        result = await search_legal_units_by_activity_codes(activity_codes=["84.23Z", "86.21Z"])
        assert result is not None

    async def test_with_values_and_condition(self):
        result = await search_legal_units_by_activity_codes(activity_codes=["84.23Z", "86.21Z"], inclusive=True)
        assert result is not None
    