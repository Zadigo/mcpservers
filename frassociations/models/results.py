from typing import Annotated

from pydantic import BaseModel


class AssociationModel(BaseModel):
    """AssociationModel is a Pydantic model that represents information about an association."""
    id: str
    id_ex: Annotated[
        str | None, 
        "External ID"
    ]
    siret: str | None
    rup_mi: str | None
    gestion: str | None    
    date_creat: str | None
    date_decla: str | None
    date_publi: str | None
    date_disso: str | None
    nature: str | None
    groupement: str | None
    titre: str | None
    titre_court: str | None
    objet: str | None
    objet_social1: int | None
    objet_social2: int | None
    adrs_complement: str | None
    adrs_numvoie: str | None
    adrs_repetition: str | None
    adrs_typevoie: str | None
    adrs_libvoie: str | None
    adrs_distrib: str | None
    adrs_codeinsee: str | None
    adrs_codepostal: float | None
    adrs_libcommune: str | None
    adrg_declarant: str | None
    adrg_complemid: str | None
    adrg_complemgeo: str | None
    adrg_libvoie: str | None
    adrg_distrib: str | None
    adrg_codepostal: str | None
    adrg_achemine: str | None
    adrg_pays: str | None
    dir_civilite: str
    siteweb: str | None
    publiweb: int | None
    observation: str | None
    position: str | None
    maj_time: int | None
