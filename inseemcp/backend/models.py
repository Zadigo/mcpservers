from pydantic import BaseModel, Field


class SearchQuery(BaseModel):
    q: str = Field(default='')
    date: str = Field(default='')
    nombre: int = Field(default=20, gte=0, lte=20)
    tri: str = Field(default='')



class StartsWithQuery(BaseModel):
    """A query model for searching entities whose 
    identifiers start with a specific string.
    
    Example:

    `https://api.insee.fr/api-sirene/3.11/siret?q=siren:3*&champs=siret,denominationUniteLegale&curseur=*`
    """
    q: str = Field(default='')
    champs: list[str] = Field(default_factory=list)
    curseur: str = Field(default='*')
