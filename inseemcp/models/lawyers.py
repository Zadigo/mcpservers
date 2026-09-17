import pydantic


class LawyersModel(pydantic.BaseModel):
    civilite: str | None = pydantic.Field(
        default=None
    )
    actif_salarie: bool = pydantic.Field(
        default=False
    )
    barreau: str | None = pydantic.Field(
        default=None
    )
    barreau_id: str | None = pydantic.Field(
        default=None
    )
    av_cnbf_code: str | None = pydantic.Field(
        default=None
    )
    av_lang: str | None = pydantic.Field(
        default=None
    )
    nom: str | None = pydantic.Field(
        default=None
    )
    prenom: str | None = pydantic.Field(
        default=None
    )
    av_bar_entree: int | None = pydantic.Field(
        default=None
    )
    cb_adresse_1: str | None = pydantic.Field(
        default=None
    )
    cb_adresse_2: str | None = pydantic.Field(
        default=None
    )
    cb_cp: str | None = pydantic.Field(
        default=None
    )
    cb_ville: str | None = pydantic.Field(
        default=None
    )
    cb_tel: str | None = pydantic.Field(
        default=None
    )
    cb_fax: str | None = pydantic.Field(
        default=None
    )
    cb_siret_siren: str | None = pydantic.Field(
        default=None
    )
    cb_siret_nic: str | None = pydantic.Field(
        default=None
    )
    cb_raison_sociale: str | None = pydantic.Field(
        default=None
    )
    ac_date_entree: int | None = pydantic.Field(
        default=None
    )
    cb_form_juri: str | None = pydantic.Field(
        default=None
    )
    av_mel_ordre: str | None = pydantic.Field(
        default=None
    )
    sp_libelle_1: str | None = pydantic.Field(
        default=None
    )
    sp_libelle_2: str | None = pydantic.Field(
        default=None
    )
    sp_libelle_3: str | None = pydantic.Field(
        default=None
    )
    ac_date_serment: str | None = pydantic.Field(
        default=None
    )
    av_date_exer: int | None = pydantic.Field(
        default=None
    )
    av_inscription: float | None = pydantic.Field(
        default=None
    )
