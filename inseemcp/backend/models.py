from typing import Any

import pydantic


class ResponseErrorModel(pydantic.BaseModel):
    status_code: int
    content: str
    json_content: dict[str, Any] | None = None
