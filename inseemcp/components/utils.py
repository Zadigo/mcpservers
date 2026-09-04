from fastmcp.tools import ToolResult

from backend.simple_requester import (
    Requester,
)
from utils import logger


def select_response(instance: Requester):
    meta = {
        "searched": "unités légales",
        "url": instance._final_url
    }
    
    if instance.has_error:
        logger.error(f"Error occurred while processing the request: {instance.error.content}")
        return ToolResult(
            content=instance.error.content, 
            meta=meta,
            is_error=True
        )

    return ToolResult(
        structured_content=instance._cached_response, 
        meta=meta
    )
