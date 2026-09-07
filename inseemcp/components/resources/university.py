
from fastmcp.resources import ResourceContent, ResourceResult, resource

from backend.base import UniversityRequest


@resource("dataset://available-universities")
async def get_universities_resource():
    instance = UniversityRequest()
    await instance()

    if instance._cached_response is None:
        return ResourceResult(
            contents=[
                ResourceContent(
                    content={"error": "Failed to fetch universities data"}
                )
            ]
        )

    return ResourceResult(
        contents=[
            ResourceContent(
                content=instance._cached_response.json()[:10]
            )
        ]
    )
