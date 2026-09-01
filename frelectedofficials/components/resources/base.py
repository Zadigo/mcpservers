import aiofiles
from fastmcp.resources import resource

from utils import BASE_DIR


@resource('file:///components/resources/templates/data-gouv.md')
async def global_dataset_information():
    """Get information about the global datasets."""
    fullpath = BASE_DIR / 'components/resources/templates/data-gouv.md'

    try:
        async with aiofiles.open(fullpath, mode="r") as f:
            content = await f.read()
        return content
    except FileNotFoundError:
        return "Resource not found: data-gouv.md"
    
    # with fullpath.open('r') as f:
    #     return ResourceResult(
    #         contents=[
    #             ResourceContent(
    #                 content=f.read(), 
    #                 mime_type="text/markdown"
    #             ),
    #         ],
    #         meta={"total": 1}
    #     )
