
from pydantic import BaseModel, Field


class SingleSearchQuery(BaseModel):
    siren: str = Field(description='SIREN of the business')
    date: str | None = Field(default_value=None)


class MultiCriteriaSearchQuery(BaseModel):
    q: str = Field(default='')
    date: str | None = Field(default=None)
    tri: str | None = Field(default=None)
    nombre: int = Field(default=20, ge=0, le=20)


class StartsWithQuery(BaseModel):
    q: str = Field(default='')
    champs: list[str] = Field(default_factory=list)
    curseur: str = Field(default='*')
