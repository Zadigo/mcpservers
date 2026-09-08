import enum

import pydantic
from pydantic import Field


class AddressModel(pydantic.BaseModel):
    complementAdresseEtablissement: str | None = Field(
        default=None,
        description="Complément d'adresse de l'établissement"
    )
    numeroVoieEtablissement: str | None = Field(
        default=None,
        description="Numéro de voie de l'établissement"
    )
    indiceRepetitionEtablissement: str | None = Field(
        default=None,
        description="Indice de répétition de l'établissement"
    )
    dernierNumeroVoieEtablissement: str | None = Field(
        default=None,
        description="Dernier numéro de voie de l'établissement"
    )
    indiceRepetitionDernierNumeroVoieEtablissement: str | None = Field(
        default=None, 
        description="Indice de répétition du dernier numéro de voie de l'établissement"
    )
    typeVoieEtablissement: str | None = Field(
        default=None,
        description="Type de voie de l'établissement"
    )
    libelleVoieEtablissement: str | None = Field(
        default=None,
        description="Libellé de la voie de l'établissement"
    )
    codePostalEtablissement: str | None = Field(
        default=None,
        description="Code postal de l'établissement"
    )
    libelleCommuneEtablissement: str | None = Field(
        default=None,
        description="Libellé de la commune de l'établissement"
    )
    libelleCommuneEtrangerEtablissement: str | None = Field(
        default=None,
        description="Libellé de la commune étrangère de l'établissement"
    )
    distributionSpecialeEtablissement: str | None = Field(
        default=None,
        description="Distribution spéciale de l'établissement"
    )
    codeCommuneEtablissement: str | None = Field(
        default=None,
        description="Code commune de l'établissement"
    )
    codeCedexEtablissement: str | None = Field(
        default=None,
        description="Code CEDEX de l'établissement"
    )
    libelleCedexEtablissement: str | None = Field(
        default=None,
        description="Libellé CEDEX de l'établissement"
    )
    codePaysEtrangerEtablissement: str | None = Field(
        default=None,
        description="Code pays étranger de l'établissement"
    )
    libellePaysEtrangerEtablissement: str | None = Field(
        default=None,
        description="Libellé pays étranger de l'établissement"
    )
    identifiantAdresseEtablissement: str | None = Field(
        default=None,
        description="Identifiant de l'adresse de l'établissement"
    )
    coordonneeLambertAbscisseEtablissement: str | None = Field(
        default=None,
        description="Coordonnée Lambert abscisse de l'établissement"
    )
    coordonneeLambertOrdonneeEtablissement: str | None = Field(
        default=None,
        description="Coordonnée Lambert ordonnée de l'établissement"
    )


class Address2Model(pydantic.BaseModel):
    complementAdresse2Etablissement: str | None = Field(
        default=None,
        description="Complément d'adresse de l'établissement"
    )
    numeroVoie2Etablissement: str | None = Field(
        default=None,
        description="Numéro de voie de l'établissement"
    )
    indiceRepetition2Etablissement: str | None = Field(
        default=None,
        description="Indice de répétition de l'établissement"
    )
    dernierNumeroVoie2Etablissement: str | None = Field(
        default=None,
        description="Dernier numéro de voie de l'établissement"
    )
    indiceRepetitionDernierNumeroVoie2Etablissement: str | None = Field(
        default=None,
        description="Indice de répétition du dernier numéro de voie de l'établissement"
    )
    typeVoie2Etablissement: str | None = Field(
        default=None,
        description="Type de voie de l'établissement"
    )
    libelleVoie2Etablissement: str | None = Field(
        default=None,
        description="Libellé de la voie de l'établissement"
    )
    codePostal2Etablissement: str | None = Field(
        default=None,
        description="Code postal de l'établissement"
    )
    libelleCommune2Etablissement: str | None = Field(
        default=None,
        description="Libellé de la commune de l'établissement"
    )
    libelleCommuneEtranger2Etablissement: str | None = Field(
        default=None,
        description="Libellé de la commune étrangère de l'établissement"
    )
    distributionSpeciale2Etablissement: str | None = Field(
        default=None,
        description="Distribution spéciale de l'établissement"
    )
    codeCommune2Etablissement: str | None = Field(
        default=None,
        description="Code commune de l'établissement"
    )
    codeCedex2Etablissement: str | None = Field(
        default=None,
        description="Code CEDEX de l'établissement"
    )
    libelleCedex2Etablissement: str | None = Field(
        default=None,
        description="Libellé CEDEX de l'établissement"
    )
    codePaysEtranger2Etablissement: str | None = Field(
        default=None,
        description="Code pays étranger de l'établissement"
    )
    libellePaysEtranger2Etablissement: str | None = Field(
        default=None,
        description="Libellé pays étranger de l'établissement"
    )
    identifiantAdresse2Etablissement: str | None = Field(
        default=None,
        description="Identifiant de l'adresse de l'établissement"
    )
    coordonneeLambertAbscisse2Etablissement: str | None = Field(
        default=None,
        description="Coordonnée Lambert abscisse de l'établissement"
    )
    coordonneeLambertOrdonnee2Etablissement: str | None = Field(
        default=None,
        description="Coordonnée Lambert ordonnée de l'établissement"
    )



class LegalUnitModel(pydantic.BaseModel):
    etatAdministratifUniteLegale: str = Field(
        description="Administrative status of the legal unit"
    )
    statutDiffusionUniteLegale: str = Field(
        description="Indicates if the legal unit is public or if its dissemination is restricted. One of 'O' (Open) or 'P' (Restricted or partially restricted)"
    )
    dateCreationUniteLegale: str = Field(
        description="Date on which the legal unit was created"
    )
    categorieJuridiqueUniteLegale: str = Field(
        description="Legal category of the legal unit"
    )
    denominationUniteLegale: str = Field(
        description="Legal unit's legal name"
    )
    sigleUniteLegale: str | None = Field(
        default=None,
        description="Acronym of the legal unit"
    )
    denominationUsuelle1UniteLegale: str | None = Field(
        default=None, 
        description="First usual name of the legal unit"
    )
    denominationUsuelle2UniteLegale: str | None = Field(
        default=None, 
        description="Second usual name of the legal unit"
    )
    denominationUsuelle3UniteLegale: str | None = Field(
        default=None, 
        description="Third usual name of the legal unit"
    )
    sexeUniteLegale: str | None = Field(
        default=None, 
        description="Sex of the legal unit"
    )
    nomUniteLegale: str | None = Field(
        default=None, 
        description="Surname of the legal unit"
    )
    nomUsageUniteLegale: str | None = Field(
        default=None, 
        description="Usual surname of the legal unit"
    )
    prenom1UniteLegale: str | None = Field(
        default=None, 
        description="First given name of the legal unit"
    )
    prenom2UniteLegale: str | None = Field(
        default=None, 
        description="Second given name of the legal unit"
    )
    prenom3UniteLegale: str | None = Field(
        default=None, 
        description="Third given name of the legal unit"
    )
    prenom4UniteLegale: str | None = Field(
        default=None, 
        description="Fourth given name of the legal unit"
    )
    prenomUsuelUniteLegale: str | None = Field(
        default=None, 
        description="Usual given name of the legal unit"
    )
    pseudonymeUniteLegale: str | None = Field(
        default=None, 
        description="Pseudonym of the legal unit"
    )
    activitePrincipaleUniteLegale: str | None = Field(
        default=None, 
        description="Main activity of the legal unit"
    )
    nomenclatureActivitePrincipaleUniteLegale: str | None = Field(
        default=None, 
        description="Classification used for the legal unit's main activity"
    )
    identifiantAssociationUniteLegale: str | None = Field(
        default=None, 
        description="Association identifier of the legal unit"
    )
    economieSocialeSolidaireUniteLegale: str | None = Field(
        default=None, 
        description="Social and solidarity economy status of the legal unit"
    )
    societeMissionUniteLegale: str | None = Field(
        default=None, 
        description="Mission-driven company status of the legal unit"
    )
    caractereEmployeurUniteLegale: str | None = Field(
        default=None, 
        description="Employer status of the legal unit"
    )
    trancheEffectifsUniteLegale: str = Field(
        description="Employee count range of the legal unit"
    )

    anneeEffectifsUniteLegale: str = Field(
        description="Year to which the legal unit's employee count relates"
    )
    nicSiegeUniteLegale: str = Field(
        description="NIC identifying the legal unit's head-office establishment"
    )
    dateDernierTraitementUniteLegale: str = Field(
        description="Date of the last processing of the legal unit's data"
    )
    categorieEntreprise: str = Field(
        description="Enterprise category"
    )
    anneeCategorieEntreprise: str = Field(
        description="Year of the enterprise category"
    )
    activitePrincipaleNAF25UniteLegale: str = Field(
        description="Main activity of the legal unit according to NAF 2025"
    )
    

class LegalUnitPeriodModel(pydantic.BaseModel):
    dateFin: str | None = Field(
        default=None,
        description="End date of the legal unit period",
    )
    dateDebut: str = Field(
        description="Start date of the legal unit period",
    )
    etatAdministratifEtablissement: str = Field(
        description="Indicates whether a business or legal unit is active or ceased: 'A' for active, 'C' for ceased",
    )
    changementEtatAdministratifEtablissement: bool = Field(
        default=False,
        description="Indicates whether the administrative status of the establishment has changed",
    )
    enseigne1Etablissement: str = Field(
        description="Primary trading name of the establishment",
    )
    enseigne2Etablissement: str | None = Field(
        default=None,
        description="Secondary trading name of the establishment",
    )
    enseigne3Etablissement: str | None = Field(
        default=None,
        description="Third trading name of the establishment",
    )
    changementEnseigneEtablissement: bool = Field(
        default=False,
        description="Indicates whether the trading name of the establishment has changed",
    )
    denominationUsuelleEtablissement: str | None = Field(
        default=None,
        description="Usual name of the establishment",
    )
    changementDenominationUsuelleEtablissement: bool = Field(
        default=False,
        description="Indicates whether the usual name of the establishment has changed",
    )
    activitePrincipaleEtablissement: str | None = Field(
        default=None,
        description="Main activity of the establishment",
    )
    nomenclatureActivitePrincipaleEtablissement: str | None = Field(
        default=None,
        description="Classification used for the establishment's main activity",
    )
    changementActivitePrincipaleEtablissement: bool = Field(
        default=False,
        description="Indicates whether the main activity of the establishment has changed",
    )
    caractereEmployeurEtablissement: str | None = Field(
        default=None,
        description="Employer status of the establishment",
    )
    changementCaractereEmployeurEtablissement: bool = Field(
        default=False,
        description="Indicates whether the employer status of the establishment has changed",
    )

class EstablishmentModel(pydantic.BaseModel):
    siren: str = Field(
        description="SIREN of the legal unit to which the establishment belongs"
    )
    nic: str = Field(
        description="NIC identifying the establishment"
    )
    siret: str = Field(
        description="SIRET identifying the establishment"
    )
    statutDiffusionEtablissement: str = Field(
        description="Indicates if the establishment is public or if its dissemination is restricted: 'O' (Open) or 'P' (Restricted or partially restricted)"
    )
    dateCreationEtablissement: str = Field(
        description="Date on which the establishment was created"
    )
    trancheEffectifsEtablissement: str = Field(
        description="Employee count range of the establishment"
    )
    anneeEffectifsEtablissement: str | None = Field(
        default=None,
        description="Year to which the establishment's employee count relates"
    )
    activitePrincipaleEtablissement: str | None = Field(
        default=None,
        description="Main activity of the establishment"
    )
    dateDernierTraitementEtablissement: str = Field(
        description="Date of the last processing of the establishment's data"
    )
    etablissementSiege: bool = Field(
        description="Indicates whether the establishment is the head office"
    )
    nombrePeriodesEtablissement: int = Field(
        description="Number of periods recorded for the establishment"
    )
    activitePrincipaleNAF25Etablissement: str = Field(
        description="Main activity of the establishment according to NAF 2025"
    )
    uniteLegale: LegalUnitModel = Field(
        description="Legal unit to which the establishment belongs"
    )
    adresseEtablissement: AddressModel = Field(
        description="Address of the establishment"
    )
    adresse2Etablissement: Address2Model = Field(
        description="Secondary address of the establishment"
    )
    periodesEtablissement: list[LegalUnitPeriodModel] = Field(
        description="List of periods recorded for the establishment"
    )


class HeaderModel(pydantic.BaseModel):
    statut: int = Field(
        description="Statut of the response"
    )
    message: str = Field(
        description="Message of the response"
    )
    total: int = Field(
        default=0,
        description="Total number of results"
    )
    debut: int = Field(
        default=0,
        description="Starting index of the results"
    )
    nombre: int = Field(
        default=0,
        description="Number of results returned in the response"
    )


class BaseResponseModel(pydantic.BaseModel):
    header: HeaderModel = Field(
        description="Header of the response"
    )
    etablissements: list[EstablishmentModel] = Field(
        description="List of establishments in the response"
    )


class BusinessColumnEnum(enum.Enum):
    ACTIVITE_PRINCIPALE_ETABLISSEMENT = "activitePrincipaleEtablissement"
    ACTIVITE_PRINCIPALE_NAF25_ETABLISSEMENT = "activitePrincipaleNAF25Etablissement"
    ACTIVITE_PRINCIPALE_NAF25_UNITE_LEGALE = "activitePrincipaleNAF25UniteLegale"
    ACTIVITE_PRINCIPALE_UNITE_LEGALE = "activitePrincipaleUniteLegale"
    ADRESSE2_ETABLISSEMENT = "adresse2Etablissement"
    ADRESSE_ETABLISSEMENT = "adresseEtablissement"
    ANNEE_CATEGORIE_ENTREPRISE = "anneeCategorieEntreprise"
    ANNEE_EFFECTIFS_ETABLISSEMENT = "anneeEffectifsEtablissement"
    ANNEE_EFFECTIFS_UNITE_LEGALE = "anneeEffectifsUniteLegale"
    CARACTERE_EMPLOYEUR_UNITE_LEGALE = "caractereEmployeurUniteLegale"
    CATEGORIE_ENTREPRISE = "categorieEntreprise"
    CATEGORIE_JURIDIQUE_UNITE_LEGALE = "categorieJuridiqueUniteLegale"
    CODE_POSTAL_ETABLISSEMENT = "codePostalEtablissement"
    DATE_CREATION_ETABLISSEMENT = "dateCreationEtablissement"
    DATE_CREATION_UNITE_LEGALE = "dateCreationUniteLegale"
    DATE_DERNIER_TRAITEMENT_ETABLISSEMENT = "dateDernierTraitementEtablissement"
    DATE_DERNIER_TRAITEMENT_UNITE_LEGALE = "dateDernierTraitementUniteLegale"
    DENOMINATION_UNITE_LEGALE = "denominationUniteLegale"
    DENOMINATION_USUELLE_UNITE_LEGALE = "denominationUsuelleUniteLegale"
    DENOMINATION_USUELLE1_UNITE_LEGALE = "denominationUsuelle1UniteLegale"
    DENOMINATION_USUELLE2_UNITE_LEGALE = "denominationUsuelle2UniteLegale"
    DENOMINATION_USUELLE3_UNITE_LEGALE = "denominationUsuelle3UniteLegale"
    ECONOMIE_SOCIALE_SOLIDAIRE_UNITE_LEGALE = "economieSocialeSolidaireUniteLegale"
    ETABLISSEMENT_SIEGE = "etablissementSiege"
    ETAT_ADMINISTRATIF_ETABLISSEMENT = "etatAdministratifEtablissement"
    ETAT_ADMINISTRATIF_UNITE_LEGALE = "etatAdministratifUniteLegale"
    IDENTIFIANT_ASSOCIATION_UNITE_LEGALE = "identifiantAssociationUniteLegale"
    LIBELLE_VOIE_ETABLISSEMENT = "libelleVoieEtablissement"
    NIC = "nic"
    NIC_SIEGE_UNITE_LEGALE = "nicSiegeUniteLegale"
    NOM_UNITE_LEGALE = "nomUniteLegale"
    NOM_USAGE_UNITE_LEGALE = "nomUsageUniteLegale"
    NOMBRE_PERIODES_ETABLISSEMENT = "nombrePeriodesEtablissement"
    NOMENCLATURE_ACTIVITE_PRINCIPALE_UNITE_LEGALE = "nomenclatureActivitePrincipaleUniteLegale"
    PERIODES_ETABLISSEMENT = "periodesEtablissement"
    PRENOM1_UNITE_LEGALE = "prenom1UniteLegale"
    PRENOM2_UNITE_LEGALE = "prenom2UniteLegale"
    PRENOM3_UNITE_LEGALE = "prenom3UniteLegale"
    PRENOM4_UNITE_LEGALE = "prenom4UniteLegale"
    PRENOM_USUEL_UNITE_LEGALE = "prenomUsuelUniteLegale"
    PSEUDONYME_UNITE_LEGALE = "pseudonymeUniteLegale"
    SEXE_UNITE_LEGALE = "sexeUniteLegale"
    SIGLE_UNITE_LEGALE = "sigleUniteLegale"
    SIREN = "siren"
    SIRET = "siret"
    SOCIETE_MISSION_UNITE_LEGALE = "societeMissionUniteLegale"
    STATUT_DIFFUSION_ETABLISSEMENT = "statutDiffusionEtablissement"
    STATUT_DIFFUSION_UNITE_LEGALE = "statutDiffusionUniteLegale"
    TRANCHE_EFFECTIFS_ETABLISSEMENT = "trancheEffectifsEtablissement"
    TRANCHE_EFFECTIFS_UNITE_LEGALE = "trancheEffectifsUniteLegale"
    UNITE_LEGALE = "uniteLegale"
