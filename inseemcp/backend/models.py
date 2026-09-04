from pydantic import BaseModel, Field

from backend.operators import KeyValuePair


class SingleSearchQuery(BaseModel):
    siren_ou_siret: str | None = Field(
        default=None,
        description='SIREN or SIRET of the business'
    )
    date: str | None = Field(
        default=None,
        description='Period of the SIREN or SIRET number to search for.'
    )


class MultiCriteriaSearchQuery(BaseModel):
    q: str | KeyValuePair = Field(
        default='',
        description='Query string for multi-criteria search',
    )
    date: str | None = Field(
        default=None
    )
    tri: str | None = Field(
        default=None,
        description='Sorting criteria for the search results',
    )
    nombre: int = Field(
        default=20, 
        ge=0, 
        le=20
    )
