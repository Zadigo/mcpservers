import pytest

from endpoints import ConcreteDistrictCouncillor, generate_elected_officials


@pytest.mark.parametrize(
    'klass', 
    [
        ConcreteDistrictCouncillor,
    ]
)
async def test_district_councillor_get_dataframe(klass):
    result = await generate_elected_officials(klass())
    
    assert result is not None
    assert not result.empty



async def test_elected_officials_fetch_csv(elected_officials):
    result = await elected_officials.fetch_csv_file()
    assert result is not None  


async def test_fetch_cache_or_csv(elected_officials):
    result = await elected_officials.fetch_cache_or_csv(force_clear_cache=True)
    assert result is not None  
