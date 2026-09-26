import pydantic


class BodaccQuery(pydantic.BaseModel):
    where: str | None = None
    limit: int | None = None
    offset: int | None = None
