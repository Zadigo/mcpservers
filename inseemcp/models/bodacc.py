import json
from typing import Annotated

from pydantic import BaseModel, Field, model_validator
from pydantic.functional_validators import AfterValidator


class EstablishmentModel(BaseModel):
    origineFonds: str | None = Field(
        None,
        description="The origin of the funds for the establishment."
    )
    qualiteEtablissement: str | None = Field(
        None,
        description="The quality of the establishment (e.g., principal establishment)."
    )
    activite: str | None = Field(
        None,
        description="The activity of the establishment."
    )
    adresse: AddressModel | None = Field(
        None,
        description="The address of the establishment."
    )


class AddressModel(BaseModel):
    numeroVoie: str | None = Field(
        None,
        description="The street number of the person's address."
    )
    typeVoie: str | None = Field(
        None,
        description="The type of street (e.g., rue, avenue) of the person's address."
    )
    nomVoie: str | None = Field(
        None,
        description="The name of the street of the person's address."
    )
    codePostal: str | None = Field(
        None,
        description="The postal code of the person's address."
    )
    ville: str | None = Field(
        None,
        description="The city of the person's address."
    )
    pays: str | None = Field(
        None,
        description="The country of the person's address."
    )


class PersonRegistrationInfoModel(BaseModel):
    numeroIdentification: str | None = Field(
        None,
        description="The identification number associated with the person's registration."
    )
    codeRCS: str | None = Field(
        None,
        description="The RCS code associated with the person's registration."
    )
    nomGreffeImmat: str | None = Field(
        None,
        description="The name of the registry office associated with the person's registration."
    )


class PersonModel(BaseModel):
    typePersonne: str | None = Field(
        None,
        description="The type of person (e.g., pm) associated with the Bodacc entry."
    )
    numeroImmatriculation: PersonRegistrationInfoModel | None = Field(
        None,
        description="The registration number details associated with the Bodacc entry."
    )
    denomination: str | None = Field(
        None,
        description="The denomination associated with the Bodacc entry."
    )
    sigle: str | None = Field(
        None,
        description="The acronym associated with the Bodacc entry."
    )
    formeJuridique: str | None = Field(
        None,
        description="The legal form associated with the Bodacc entry."
    )
    adresseSiegeSocial: AddressModel | None = Field(
        None,
        description="The address of the registered office associated with the Bodacc entry."
    )


class BodaccPersonModel(BaseModel):
    personne: PersonModel | None = Field(
        None,
        description="The person associated with the Bodacc entry."
    )


class BodaccModel(BaseModel):
    id: str | None = Field(
        None,
        description="The unique identifier for the Bodacc entry."
    )
    publicationavis: str | None = Field(
        None,
        description="The publication notice type for the Bodacc entry: C, B, etc."
    )
    parution: str | None = Field(
        None,
        description="The publication date for the Bodacc entry."
    )
    dateparution: str | None = Field(
        None,
        description="The publication date for the Bodacc entry."
    )
    numeroannonce: int | None = Field(
        None,
        description="The announcement number for the Bodacc entry."
    )
    typeavis: str | None = Field(
        None,
        description="The type of notice for the Bodacc entry."
    )
    typeavis_lib: str | None = Field(
        None,
        description="The type of notice for the Bodacc entry (human-readable)."
    )
    familleavis: str | None = Field(
        None,
        description="The family of notice for the Bodacc entry."
    )
    numerodepartement: str | None = Field(
        None,
        description="The department number for the Bodacc entry."
    )
    departement_nom_officiel: str | None = Field(
        None,
        description="The official name of the department for the Bodacc entry."
    )
    region_code: int | None = Field(
        None,
        description="The region code for the Bodacc entry."
    )
    region_nom_officiel: str | None = Field(
        None,
        description="The official name of the region for the Bodacc entry."
    )
    tribunal: str | None = Field(
        None,
        description="The court where the Bodacc entry was published."
    )
    commercant: str | None = Field(
        None,
        description="The merchant associated with the Bodacc entry."
    )
    ville: str | None = Field(
        None,
        description="The city associated with the Bodacc entry."
    )
    registre: list[str] | None = Field(
        None,
        description="The SIREN/SIRET associated with the Bodacc entry."
    )
    cp: str | None = Field(
        None,
        description="The postal code associated with the Bodacc entry."
    )
    pdf_parution_subfolder: int | None = Field(
        None,
        description="The subfolder for the PDF of the publication associated with the Bodacc entry."
    )
    ispdf_unitaire: str | None = Field(
        None,
        description="Indicates whether the PDF of the publication is unitary for the Bodacc entry."
    )
    listepersonnes: BodaccPersonModel | None = Field(
        None,
        description="The list of people associated with the Bodacc entry."
    )
    listeetablissements: EstablishmentModel | None = Field(
        None,
        description="The list of establishments associated with the Bodacc entry."
    )
    jugement: str | None = Field(
        None,
        description="The judgment associated with the Bodacc entry."
    )
    acte: str | None = Field(
        None,
        description="The act associated with the Bodacc entry."
    )
    modificationsgenerales: str | None = Field(
        None,
        description="The general modifications associated with the Bodacc entry."
    )
    radiationaurcs: str | None = Field(
        None,
        description="The radiation au RCS associated with the Bodacc entry."
    )
    depot: str | None = Field(
        None,
        description="The deposit associated with the Bodacc entry."
    )
    listeprecedentexploitant: str | None = Field(
        None,
        description="The list of previous operators associated with the Bodacc entry."
    )
    listeprecedentproprietaire: str | None = Field(
        None,
        description="The list of previous owners associated with the Bodacc entry."
    )
    divers: str | None = Field(
        None,
        description="Miscellaneous information associated with the Bodacc entry."
    )
    parutionavisprecedent: str | None = Field(
        None,
        description="The previous notice of publication associated with the Bodacc entry."
    )
    url_complete: Annotated[str | None, AfterValidator(lambda x: x)] = Field(
        None,
        description="The complete URL associated with the Bodacc entry."
    )

    @model_validator(mode='before')
    @classmethod
    def validate_data(cls, data: dict) -> dict:
        if isinstance(data, dict):
            for key in ['listepersonnes', 'listeetablissements']:
                str_values = data.get(key)
                if str_values is None:
                    continue
                
                json_value: dict = json.loads(str_values)

                if key == 'listepersonnes':
                    data[key] = BodaccPersonModel(**json_value)
                elif key == 'listeetablissements':
                    data[key] = EstablishmentModel(**json_value)

        return data

