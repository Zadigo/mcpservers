import pydantic


class ResponseError(pydantic.BaseModel):
    status_code: int
    content: str
    json_content: dict | None = None
