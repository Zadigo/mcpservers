
from pydantic import BaseModel, Field


class AssociationModel(BaseModel):
    """AssociationModel is a Pydantic model that represents information about an association."""
    id: str = Field(
        description="Unique identifier of the association"
    )
    id_ex: str | None = Field(
        default=None,
        description="External ID of the association"
    )
    siret: str | None = Field(
        default=None,
        description="SIRET number of the association"
    )
    rup_mi: str | None = Field(
        default=None,
        description="RUP MI number of the association"
    )
    gestion: str | None = Field(
        default=None,
        description="Gestion information of the association"
    )
    date_creat: str | None = Field(
        default=None,
        description="Creation date of the association"
    )
    date_decla: str | None = Field(
        default=None,
        description="Declaration date of the association"
    )
    date_publi: str | None = Field(
        default=None,
        description="Publication date of the association"
    )
    date_disso: str | None = Field(
        default=None,
        description="Dissolution date of the association"
    )
    nature: str | None = Field(
        default=None,
        description="Nature of the association"
    )
    groupement: str | None = Field(
        default=None,
        description="Groupement of the association"
    )
    titre: str | None = Field(
        default=None,
        description="Title of the association"
    )
    titre_court: str | None = Field(
        default=None,
        description="Short title of the association"
    )
    objet: str | None = Field(
        default=None,
        description="Object of the association"
    )
    objet_social1: int | None = Field(
        default=None,
        description="First social object of the association"
    )
    objet_social2: int | None = Field(
        default=None,
        description="Second social object of the association"
    )
    adrs_complement: str | None = Field(
        default=None,
        description="Address complement of the association"
    )
    adrs_numvoie: str | None = Field(
        default=None,
        description="Address street number of the association"
    )
    adrs_repetition: str | None = Field(
        default=None,
        description="Address repetition of the association"
    )
    adrs_typevoie: str | None = Field(
        default=None,
        description="Address street type of the association"
    )
    adrs_libvoie: str | None = Field(
        default=None,
        description="Address street name of the association"
    )
    adrs_distrib: str | None = Field(
        default=None,
        description="Address distribution of the association"
    )
    adrs_codeinsee: str | None = Field(
        default=None,
        description="Address INSEE code of the association"
    )
    adrs_codepostal: float | None = Field(
        default=None,
        description="Address postal code of the association"
    )
    adrs_libcommune: str | None = Field(
        default=None,
        description="Address commune name of the association"
    )
    adrg_declarant: str | None = Field(
        default=None,
        description="Declarant of the association"
    )
    adrg_complemid: str | None = Field(
        default=None,
        description="Complementary ID of the association"
    )
    adrg_complemgeo: str | None = Field(
        default=None,
        description="Geographical complement of the association"
    )
    adrg_libvoie: str | None = Field(
        default=None,
        description="Street name of the association"
    )
    adrg_distrib: str | None = Field(
        default=None,
        description="Distribution of the association"
    )
    adrg_codepostal: str | None = Field(
        default=None,
        description="Postal code of the association"
    )
    adrg_achemine: str | None = Field(
        default=None,
        description="Routing information of the association"
    )
    adrg_pays: str | None = Field(
        default=None,
        description="Country of the association"
    )
    dir_civilite: str = Field(
        default=None,
        description="Director civility of the association"
    )
    siteweb: str | None = Field(
        default=None,
        description="Website of the association"
    )
    publiweb: int | None = Field(
        default=None,
        description="Publication web status of the association"
    )
    observation: str | None = Field(
        default=None,
        description="Observations about the association"
    )
    position: str | None = Field(
        default=None,
        description="Position of the association"
    )
    maj_time: int | None = Field(
        default=None,
        description="Last update time of the association"
    )



class ResponseModel(BaseModel):
    total: int = Field(
        default=0,
        description="Total number of associations matching the query",
        ge=0
    )
    offset: int = Field(
        default=0,
        description="Offset of the current set of results",
        ge=0
    )
    results: list[AssociationModel] = Field(
        default_factory=list
    )
