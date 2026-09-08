from collections.abc import Hashable, Sequence
from typing import Any

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
            # content=instance.error.content, 
            structured_content=instance.error.json_content,
            meta=meta,
            is_error=True
        )

    content: dict | None = instance._cached_response.json() if instance._cached_response is not None else None
    return ToolResult(
        structured_content=content, 
        meta=meta
    )


def select_response_from_data(data: Sequence[dict[str | Hashable, Any]], meta: dict[str, Any] | None = None):    
    if len(data) > 0:
        return ToolResult(
            structured_content={
                'results': data
            }, 
            meta=meta
        )
    return ToolResult(
        content="No data available", 
        meta=meta,
        is_error=True
    )


