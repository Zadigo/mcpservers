from pydantic import BaseModel, Field

from backend.operators import BaseOperator, KeyValuePair, WildCard
from backend.typings import TypeCondition


class SingleSearchQuery(BaseModel):
    siren_ou_siret: str | None = Field(
        default=None,
        description='SIREN or SIRET of the business'
    )
    date: str | None = Field(
        default=None,
        description='Period of the SIREN or SIRET number to search for.'
    )

class MultiCriteriaSearchQuery:
    """A class model for multi-criteria search queries. This class is preferred
    instead of a pydantic.BaseModel in order to pass TypeCondition and KeyValuePair
    which prevents pydantic.BaseModel to fully initialize"""
    
    def __init__(self, q: str | KeyValuePair | TypeCondition = '', date: str | None = None, tri: str | None = None, nombre: int = 20):
        if not isinstance(q, (str, KeyValuePair, BaseOperator, WildCard)):
            raise TypeError("q must be a string, KeyValuePair, BaseOperator, or WildCard")

        self.q = q
        self.date = date
        self.tri = tri
        self.nombre = nombre

    def model_dump(self, *, exclude_none: bool = False, **kwargs):
        old_result: dict = {
            'q': self.q,
            'date': self.date,
            'tri': self.tri,
            'nombre': self.nombre
        }
        new_result = {}

        if exclude_none:
            for k, v in old_result.items():
                if v is not None:
                    new_result[k] = v
        else:
            new_result: dict = old_result

        return new_result
