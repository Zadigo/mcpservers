from fastmcp.tools import ToolResult

from backend.simple_requester import (
    Requester,
)


def select_response(instance: Requester):
    meta = {
        "searched": "unités légales",
        "url": instance._final_url
    }
    
    if instance.error is not None:
        return ToolResult(
            content=instance.error.content, 
            meta=meta,
            is_error=True
        )

    content: dict | None = instance._cached_response.json() if instance._cached_response is not None else None
    return ToolResult(
        structured_content=content, 
        meta=meta
    )
