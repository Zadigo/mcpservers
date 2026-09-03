from pydantic import BaseModel, Field

from models.base import LegalUnitEnum


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


class BaseOperator(BaseModel):
    key: LegalUnitEnum = Field(default=LegalUnitEnum.NOM_UNITE_LEGALE)
    value: str = Field(default=None)

    @property
    def operator_name(self):
        return self.__class__.__name__.lower()

    def resolve(self):
        return f"{self.key.value}:{self.value}"


class AND(BaseOperator):
    pass


class OR(BaseOperator):
    pass
