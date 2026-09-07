from components.tools.base import get_association_by_title


async def test_get_association_by_title():
    result = await get_association_by_title('Femmes')
    assert result is not None
    assert len(result) > 0
