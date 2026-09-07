from typing import Any

import pydantic
from pydantic import Field, model_validator


class UniversityCoordinatesModel(pydantic.BaseModel):
    lat: float | None = Field(
        default=None
    )
    lon: float | None = Field(
        default=None
    )


class UniversityModel(pydantic.BaseModel):
    aca_id: str | None = Field(
        default=None
    )
    aca_nom: str | None = Field(
        default=None
    )
    adresse_uai: str | None = Field(
        default=None
    )
    anciens_codes_uai: str | None = Field(
        default=None
    )
    article: str | None = Field(
        default=None
    )
    boite_postale_uai: str | None = Field(
        default=None
    )
    champ_recherche: str | None = Field(
        default=None
    )
    code_postal_uai: str | None = Field(
        default=None
    )
    com_code: str | None = Field(
        default=None
    )
    com_nom: str | None = Field(
        default=None
    )
    compte_dailymotion: str | None = Field(
        default=None
    )
    compte_facebook: str | None = Field(
        default=None
    )
    compte_flickr: str | None = Field(
        default=None
    )
    compte_france_culture: str | None = Field(
        default=None
    )
    compte_github: str | None = Field(
        default=None
    )
    compte_instagram: str | None = Field(
        default=None
    )
    compte_linkedin: str | None = Field(
        default=None
    )
    compte_pinterest: str | None = Field(
        default=None
    )
    compte_scoopit: str | None = Field(
        default=None
    )
    compte_scribd: str | None = Field(
        default=None
    )
    compte_tumblr: str | None = Field(
        default=None
    )
    compte_twitter: str | None = Field(
        default=None
    )
    compte_vimeo: str | None = Field(
        default=None
    )
    compte_youtube: str | None = Field(
        default=None
    )
    coordonnees: str | None = Field(
        default=None
    )
    date_creation: str | None = Field(
        default=None
    )
    dep_id: str | None = Field(
        default=None
    )
    dep_nom: str | None = Field(
        default=None
    )
    element_fundref: str | None = Field(
        default=None
    )
    element_isni: str | None = Field(
        default=None
    )
    element_ror: str | None = Field(
        default=None
    )
    element_wikidata: str | None = Field(
        default=None
    )
    etablissement_experimental: str | None = Field(
        default=None
    )
    etablissement_id_paysage: str | None = Field(
        default=None
    )
    flux_rss: str | None = Field(
        default=None
    )
    hal: str | None = Field(
        default=None
    )
    identifiant_eter: str | None = Field(
        default=None
    )
    identifiant_idref: str | None = Field(
        default=None
    )
    identifiant_isni: str | None = Field(
        default=None
    )
    identifiant_orgref: str | None = Field(
        default=None
    )
    identifiant_pic: str | None = Field(
        default=None
    )
    identifiant_ror: str | None = Field(
        default=None
    )
    identifiant_wikidata: str | None = Field(
        default=None
    )
    inscrits: str | None = Field(
        default=None
    )
    inscrits_2010: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2011: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2012: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2013: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2014: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2015: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2016: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2017: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2018: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2019: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2020: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2021: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2022: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2023: float | None = Field(
        default=None,
        ge=0
    )
    inscrits_2024: float | None = Field(
        default=None,
        ge=0
    )
    lieu_dit_uai: str | None = Field(
        default=None
    )
    localisation: str | None = Field(
        default=None
    )
    localite_acheminement_uai: str | None = Field(
        default=None
    )
    mention_distribution: str | None = Field(
        default=None
    )
    mooc: str | None = Field(
        default=None
    )
    nom_court: str | None = Field(
        default=None
    )
    numero_telephone_uai: str | None = Field(
        default=None
    )
    pays_etranger_acheminement: str | None = Field(
        default=None
    )
    reg_id: str | None = Field(
        default=None
    )
    reg_id_old: str | None = Field(
        default=None
    )
    reg_nom: str | None = Field(
        default=None
    )
    reg_nom_old: str | None = Field(
        default=None
    )
    rna: str | None = Field(
        default=None
    )
    scanr: str | None = Field(
        default=None
    )
    secteur_d_etablissement: str | None = Field(
        default=None
    )
    sigle: str | None = Field(
        default=None
    )
    siren: str | None = Field(
        default=None
    )
    siret: str | None = Field(
        default=None
    )
    statut_juridique_court: str | None = Field(
        default=None
    )
    statut_juridique_long: str | None = Field(
        default=None
    )
    texte_de_ref_creation: str | None = Field(
        default=None
    )
    texte_de_ref_creation_lib: str | None = Field(
        default=None
    )
    type_d_etablissement: str | None = Field(
        default=None
    )
    typologie_d_universites_et_assimiles: str | None = Field(
        default=None
    )
    uai: str | None = Field(
        default=None
    )
    universites_fusionnees: str | None = Field(
        default=None
    )
    uo_lib: str | None = Field(
        default=None
    )
    uo_lib_en: str | None = Field(
        default=None
    )
    uo_lib_officiel: str | None = Field(
        default=None
    )
    url: str | None = Field(
        default=None
    )
    url_cn: str | None = Field(
        default=None
    )
    url_de: str | None = Field(
        default=None
    )
    url_en: str | None = Field(
        default=None
    )
    url_es: str | None = Field(
        default=None
    )
    url_it: str | None = Field(
        default=None
    )
    uucr_id: str | None = Field(
        default=None
    )
    uucr_nom: str | None = Field(
        default=None
    )
    vague_contractuelle: str | None = Field(
        default=None
    )
    wikipedia: str | None = Field(
        default=None
    )
    wikipedia_en: str | None = Field(
        default=None
    )

    @model_validator(mode='before')
    @classmethod
    def check_columns(cls, data: Any) -> Any:
        if isinstance(data, dict):
            pass
        return data
    