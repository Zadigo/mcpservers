import enum

import pydantic
from pydantic import Field


class AddressModel(pydantic.BaseModel):
    complementAdresseEtablissement: str = Field(description="Complément d'adresse de l'établissement")
    numeroVoieEtablissement: str = Field(description="Numéro de voie de l'établissement")
    indiceRepetitionEtablissement: str | None = Field(default=None, description="Indice de répétition de l'établissement")
    dernierNumeroVoieEtablissement: str | None = Field(default=None, description="Dernier numéro de voie de l'établissement")
    indiceRepetitionDernierNumeroVoieEtablissement: str | None = Field(default=None, description="Indice de répétition du dernier numéro de voie de l'établissement")
    typeVoieEtablissement: str = Field(description="Type de voie de l'établissement")
    libelleVoieEtablissement: str = Field(description="Libellé de la voie de l'établissement")
    codePostalEtablissement: str = Field(description="Code postal de l'établissement")
    libelleCommuneEtablissement: str | None = Field(default=None, description="Libellé de la commune de l'établissement")
    libelleCommuneEtrangerEtablissement: str | None = Field(default=None, description="Libellé de la commune étrangère de l'établissement")
    distributionSpecialeEtablissement: str | None = Field(default=None, description="Distribution spéciale de l'établissement")
    codeCommuneEtablissement: str = Field(description="Code commune de l'établissement")
    codeCedexEtablissement: str | None = Field(default=None, description="Code CEDEX de l'établissement")
    libelleCedexEtablissement: str | None = Field(default=None, description="Libellé CEDEX de l'établissement")
    codePaysEtrangerEtablissement: str | None = Field(default=None, description="Code pays étranger de l'établissement")
    libellePaysEtrangerEtablissement: str | None = Field(default=None, description="Libellé pays étranger de l'établissement")
    identifiantAdresseEtablissement: str = Field(description="Identifiant de l'adresse de l'établissement")
    coordonneeLambertAbscisseEtablissement: str = Field(description="Coordonnée Lambert abscisse de l'établissement")
    coordonneeLambertOrdonneeEtablissement: str = Field(description="Coordonnée Lambert ordonnée de l'établissement")


class Address2Model(pydantic.BaseModel):
    complementAdresse2Etablissement: str | None = Field(default=None, description="Complément d'adresse de l'établissement")
    numeroVoie2Etablissement: str | None = Field(default=None, description="Numéro de voie de l'établissement")
    indiceRepetition2Etablissement: str | None = Field(default=None, description="Indice de répétition de l'établissement")
    dernierNumeroVoie2Etablissement: str | None = Field(default=None, description="Dernier numéro de voie de l'établissement")
    indiceRepetitionDernierNumeroVoie2Etablissement: str | None = Field(default=None, description="Indice de répétition du dernier numéro de voie de l'établissement")
    typeVoie2Etablissement: str | None = Field(default=None, description="Type de voie de l'établissement")
    libelleVoie2Etablissement: str | None = Field(default=None, description="Libellé de la voie de l'établissement")
    codePostal2Etablissement: str | None = Field(default=None, description="Code postal de l'établissement")
    libelleCommune2Etablissement: str | None = Field(default=None, description="Libellé de la commune de l'établissement")
    libelleCommuneEtranger2Etablissement: str | None = Field(default=None, description="Libellé de la commune étrangère de l'établissement")
    distributionSpeciale2Etablissement: str | None = Field(default=None, description="Distribution spéciale de l'établissement")
    codeCommune2Etablissement: str | None = Field(default=None, description="Code commune de l'établissement")
    codeCedex2Etablissement: str | None = Field(default=None, description="Code CEDEX de l'établissement")
    libelleCedex2Etablissement: str | None = Field(default=None, description="Libellé CEDEX de l'établissement")
    codePaysEtranger2Etablissement: str | None = Field(default=None, description="Code pays étranger de l'établissement")
    libellePaysEtranger2Etablissement: str | None = Field(default=None, description="Libellé pays étranger de l'établissement")
    identifiantAdresse2Etablissement: str | None = Field(default=None, description="Identifiant de l'adresse de l'établissement")
    coordonneeLambertAbscisse2Etablissement: str | None = Field(default=None, description="Coordonnée Lambert abscisse de l'établissement")
    coordonneeLambertOrdonnee2Etablissement: str | None = Field(default=None, description="Coordonnée Lambert ordonnée de l'établissement")



class LegalUnitModel(pydantic.BaseModel):
    etatAdministratifUniteLegale: str = Field(description="État administratif de l'unité légale")
    statutDiffusionUniteLegale: str = Field(description="Statut de diffusion de l'unité légale")
    dateCreationUniteLegale: str = Field(description="Date de création de l'unité légale")
    categorieJuridiqueUniteLegale: str = Field(description="Catégorie juridique de l'unité légale")
    denominationUniteLegale: str = Field(description="Dénomination de l'unité légale")
    sigleUniteLegale: str = Field(description="Sigle de l'unité légale")
    denominationUsuelle1UniteLegale: str | None = Field(default=None, description="Dénomination usuelle 1 de l'unité légale")
    denominationUsuelle2UniteLegale: str | None = Field(default=None, description="Dénomination usuelle 2 de l'unité légale")
    denominationUsuelle3UniteLegale: str | None = Field(default=None, description="Dénomination usuelle 3 de l'unité légale")
    sexeUniteLegale: str | None = Field(default=None, description="Sexe de l'unité légale")
    nomUniteLegale: str | None = Field(default=None, description="Nom de l'unité légale")
    nomUsageUniteLegale: str | None = Field(default=None, description="Nom d'usage de l'unité légale")
    prenom1UniteLegale: str | None = Field(default=None, description="Prénom 1 de l'unité légale")
    prenom2UniteLegale: str | None = Field(default=None, description="Prénom 2 de l'unité légale")
    prenom3UniteLegale: str | None = Field(default=None, description="Prénom 3 de l'unité légale")
    prenom4UniteLegale: str | None = Field(default=None, description="Prénom 4 de l'unité légale")
    prenomUsuelUniteLegale: str | None = Field(default=None, description="Prénom usuel de l'unité légale")
    pseudonymeUniteLegale: str | None = Field(default=None, description="Pseudonyme de l'unité légale")
    activitePrincipaleUniteLegale: str | None = Field(default=None, description="Activité principale de l'unité légale")
    nomenclatureActivitePrincipaleUniteLegale: str | None = Field(default=None, description="Nomenclature de l'activité principale de l'unité légale")
    identifiantAssociationUniteLegale: str | None = Field(default=None, description="Identifiant de l'association de l'unité légale")
    economieSocialeSolidaireUniteLegale: str | None = Field(default=None, description="Économie sociale et solidaire de l'unité légale")
    societeMissionUniteLegale: str | None = Field(default=None, description="Société mission de l'unité légale")
    caractereEmployeurUniteLegale: str | None = Field(default=None, description="Caractère employeur de l'unité légale")
    trancheEffectifsUniteLegale: str = Field(description="Tranche effectifs de l'unité légale")
    anneeEffectifsUniteLegale: str = Field(description="Année effectifs de l'unité légale")
    nicSiegeUniteLegale: str = Field(description="NIC siège de l'unité légale")
    dateDernierTraitementUniteLegale: str = Field(description="Date du dernier traitement de l'unité légale")
    categorieEntreprise: str = Field(description="Catégorie de l'entreprise")
    anneeCategorieEntreprise: str = Field(description="Année de la catégorie de l'entreprise")
    activitePrincipaleNAF25UniteLegale: str = Field(description="Activité principale NAF 25 de l'unité légale")


class LegalUnitPeriodModel(pydantic.BaseModel):
    dateFin: str | None = Field(default=None, description="Date de fin de la période de l'unité légale")
    dateDebut: str = Field(description="Date de début de la période de l'unité légale")
    etatAdministratifEtablissement: str = Field(description="État administratif de l'établissement")
    changementEtatAdministratifEtablissement: bool = Field(default=False, description="Changement de l'état administratif de l'établissement")
    enseigne1Etablissement: str = Field(description="Enseigne 1 de l'établissement")
    enseigne2Etablissement: str | None = Field(default=None, description="Enseigne 2 de l'établissement")
    enseigne3Etablissement: str | None = Field(default=None, description="Enseigne 3 de l'établissement")
    changementEnseigneEtablissement: bool = Field(default=False, description="Changement de l'enseigne de l'établissement")
    denominationUsuelleEtablissement: str | None = Field(default=None, description="Dénomination usuelle de l'établissement")
    changementDenominationUsuelleEtablissement: bool = Field(default=False, description="Changement de la dénomination usuelle de l'établissement")
    activitePrincipaleEtablissement: str | None = Field(default=None, description="Activité principale de l'établissement")
    nomenclatureActivitePrincipaleEtablissement: str | None = Field(default=None, description="Nomenclature de l'activité principale de l'établissement")
    changementActivitePrincipaleEtablissement: bool = Field(default=False, description="Changement de l'activité principale de l'établissement")
    caractereEmployeurEtablissement: str | None = Field(default=None, description="Caractère employeur de l'établissement")
    changementCaractereEmployeurEtablissement: bool = Field(default=False, description="Changement du caractère employeur de l'établissement")



class EstablishmentModel(pydantic.BaseModel):
    siren: str = Field(description="SIREN of the establishment")
    nic: str = Field(description="NIC of the establishment")
    siret: str = Field(description="SIRET of the establishment")
    statutDiffusionEtablissement: str = Field(description="Statut de diffusion de l'établissement")
    dateCreationEtablissement: str = Field(description="Date of creation of the establishment")
    trancheEffectifsEtablissement: str = Field(description="Tranche effectifs de l'établissement")
    anneeEffectifsEtablissement: str | None = Field(default=None, description="Année effectifs de l'établissement")
    activitePrincipaleEtablissement: str | None = Field(default=None, description="Activité principale de l'établissement")
    dateDernierTraitementEtablissement: str = Field(description="Date of the last treatment of the establishment")
    etablissementSiege: bool = Field(description="Indicates if the establishment is a head office")
    nombrePeriodesEtablissement: int = Field(description="Nombre périodes de l'établissement")
    activitePrincipaleNAF25Etablissement: str = Field(description="Activité principale NAF 25 de l'établissement")
    uniteLegale: LegalUnitModel = Field(description="List of legal units associated with the establishment")
    adresseEtablissement: AddressModel = Field(description="Address of the establishment")
    adresse2Etablissement: Address2Model = Field(description="Secondary address of the establishment")
    periodesEtablissement: list[LegalUnitPeriodModel] = Field(description="List of periods associated with the establishment")


class HeaderModel(pydantic.BaseModel):
    statut: int = Field(description="Statut of the response")
    message: str = Field(description="Message of the response")
    total: int = Field(description="Total number of results")
    debut: int = Field(description="Starting index of the results")
    nombre: int = Field(description="Number of results returned in the response")


class BaseResponseModel(pydantic.BaseModel):
    header: HeaderModel = Field(description="Header of the response")
    etablissements: list[EstablishmentModel] = Field(description="List of etablissements data")


# class LegalUnitsPeriod(pydantic.BaseModel):
#     dateFin: str = Field(description="Date de fin de la période de l'unité légale")
#     dateDebut: str = Field(description="Date de début de la période de l'unité légale")
#     etatAdministratifUniteLegale: str = Field(description="État administratif de l'unité légale")
#     changementEtatAdministratifUniteLegale: bool = Field(description="Indique si l'état administratif de l'unité légale a changé")
#     nomUniteLegale: str = Field(description="Nom de l'unité légale")
#     changementNomUniteLegale: bool = Field(description="Indique si le nom de l'unité légale a changé")
#     nomUsageUniteLegale: str = Field(description="Nom d'usage de l'unité légale")
#     changementNomUsageUniteLegale: bool = Field(description="Indique si le nom d'usage de l'unité légale a changé")
#     denominationUniteLegale: str = Field(description="Dénomination de l'unité légale")
#     changementDenominationUniteLegale: bool = Field(description="Indique si la dénomination de l'unité légale a changé")
#     denominationUsuelle1UniteLegale: str = Field(description="Dénomination usuelle 1 de l'unité légale")
#     denominationUsuelle2UniteLegale: str = Field(description="Dénomination usuelle 2 de l'unité légale")
#     denominationUsuelle3UniteLegale: str = Field(description="Dénomination usuelle 3 de l'unité légale")
#     categorieJuridiqueUniteLegale: str = Field(description="Catégorie juridique de l'unité légale")
#     changementCategorieJuridiqueUniteLegale: bool = Field(description="Indique si la catégorie juridique de l'unité légale a changé")
#     activitePrincipaleUniteLegale: str = Field(description="Activité principale de l'unité légale")
#     nomenclatureActivitePrincipaleUniteLegale: str = Field(description="Nomenclature de l'activité principale de l'unité légale")
#     changementActivitePrincipaleUniteLegale: bool = Field(description="Indique si l'activité principale de l'unité légale a changé")
#     nicSiegeUniteLegale: str = Field(description="NIC du siège de l'unité légale")
#     changementNicSiegeUniteLegale: bool = Field(description="Indique si le NIC du siège de l'unité légale a changé")
#     economieSocialeSolidaireUniteLegale: str = Field(description="Économie sociale et solidaire de l'unité légale")
#     changementEconomieSocialeSolidaireUniteLegale: bool = Field(description="Indique si l'économie sociale et solidaire de l'unité légale a changé")
#     societeMissionUniteLegale: str = Field(description="Société mission de l'unité légale")
#     changementSocieteMissionUniteLegale: bool = Field(description="Indique si la société mission de l'unité légale a changé")
#     caractereEmployeurUniteLegale: str = Field(description="Caractère employeur de l'unité légale")
#     changementCaractereEmployeurUniteLegale: bool = Field(description="Indique si le caractère employeur de l'unité légale a changé")
#     changementDenominationUsuelleUniteLegale: bool = Field(description="Indique si la dénomination usuelle de l'unité légale a changé")


# class LegalUnits(pydantic.BaseModel):
#     """A legal unit according to INSEE's SIRENE database. This model represents 
#     the structure of a legal unit, including its various attributes and characteristics."""

#     score: float = Field(description="Score de la correspondance entre la recherche et l'unité légale")
#     siren: str = Field(description="SIREN de l'unité légale")
#     statutDiffusionUniteLegale: str = Field(description="Statut de diffusion de l'unité légale")
#     unitePurgeeUniteLegale: bool = Field(description="Indique si l'unité légale est purgée")
#     dateCreationUniteLegale: str = Field(description="Date de création de l'unité légale")
#     dateNaissanceUniteLegale: str = Field(description="Date de naissance de l'unité légale")
#     codeCommuneNaissanceUniteLegale: str = Field(description="Code commune de naissance de l'unité légale")
#     codePaysNaissanceUniteLegale: str = Field(description="Code pays de naissance de l'unité légale")
#     libelleNationaliteUniteLegale: str = Field(description="Libellé nationalité de l'unité légale")
#     identifiantAssociationUniteLegale: str = Field(description="Identifiant association de l'unité légale")
#     trancheEffectifsUniteLegale: str = Field(description="Tranche effectifs de l'unité légale")
#     anneeEffectifsUniteLegale: str = Field(description="Année effectifs de l'unité légale")
#     dateDernierTraitementUniteLegale: str = Field(description="Date dernier traitement de l'unité légale")
#     nombrePeriodesUniteLegale: int = Field(description="Nombre périodes de l'unité légale")
#     categorieEntreprise: str = Field(description="Catégorie entreprise de l'unité légale")
#     anneeCategorieEntreprise: str = Field(description="Année catégorie entreprise de l'unité légale")
#     sigleUniteLegale: str = Field(description="Sigle de l'unité légale")
#     sexeUniteLegale: str = Field(description="Sexe de l'unité légale")
#     prenom1UniteLegale: str = Field(description="Prénom 1 de l'unité légale")
#     prenom2UniteLegale: str = Field(description="Prénom 2 de l'unité légale")
#     prenom3UniteLegale: str = Field(description="Prénom 3 de l'unité légale")
#     prenom4UniteLegale: str = Field(description="Prénom 4 de l'unité légale")
#     prenomUsuelUniteLegale: str = Field(description="Prénom usuel de l'unité légale")
#     pseudonymeUniteLegale: str = Field(description="Pseudonyme de l'unité légale")
#     activitePrincipaleNAF25UniteLegale: str = Field(description="Activité principale NAF 25 de l'unité légale")


class LegalUnitEnum(enum.Enum):
    DATE_FIN = 'dateFin'
    DATE_DEBUT = 'dateDebut'
    ETAT_ADMINISTRATIF_UNITE_LEGALE = 'etatAdministratifUniteLegale'
    CHANGEMENT_ETAT_ADMINISTRATIF_UNITE_LEGALE = 'changementEtatAdministratifUniteLegale'
    NOM_UNITE_LEGALE = 'nomUniteLegale'
    CHANGEMENT_NOM_UNITE_LEGALE = 'changementNomUniteLegale'
    NOM_USAGE_UNITE_LEGALE = 'nomUsageUniteLegale'
    CHANGEMENT_NOM_USAGE_UNITE_LEGALE = 'changementNomUsageUniteLegale'
    DENOMINATION_UNITE_LEGALE = 'denominationUniteLegale'
    CHANGEMENT_DENOMINATION_UNITE_LEGALE = 'changementDenominationUniteLegale'
    DENOMINATION_USUELLE_1_UNITE_LEGALE = 'denominationUsuelle1UniteLegale'
    DENOMINATION_USUELLE_2_UNITE_LEGALE = 'denominationUsuelle2UniteLegale'
    DENOMINATION_USUELLE_3_UNITE_LEGALE = 'denominationUsuelle3UniteLegale'
    CATEGORIE_JURIDIQUE_UNITE_LEGALE = 'categorieJuridiqueUniteLegale'
    CHANGEMENT_CATEGORIE_JURIDIQUE_UNITE_LEGALE = 'changementCategorieJuridiqueUniteLegale'
    ACTIVITE_PRINCIPALE_UNITE_LEGALE = 'activitePrincipaleUniteLegale'
    NOMENCLATURE_ACTIVITE_PRINCIPALE_UNITE_LEGALE = 'nomenclatureActivitePrincipaleUniteLegale'
    CHANGEMENT_ACTIVITE_PRINCIPALE_UNITE_LEGALE = 'changementActivitePrincipaleUniteLegale'
    NIC_SIEGE_UNITE_LEGALE = 'nicSiegeUniteLegale'
    CHANGEMENT_NIC_SIEGE_UNITE_LEGALE = 'changementNicSiegeUniteLegale'
    ECONOMIE_SOCIALE_SOLIDAIRE_UNITE_LEGALE = 'economieSocialeSolidaireUniteLegale'
    CHANGEMENT_ECONOMIE_SOCIALE_SOLIDAIRE_UNITE_LEGALE = 'changementEconomieSocialeSolidaireUniteLegale'
    SOCIETE_MISSION_UNITE_LEGALE = 'societeMissionUniteLegale'
    CHANGEMENT_SOCIETE_MISSION_UNITE_LEGALE = 'changementSocieteMissionUniteLegale'
    CARACTERE_EMPLOYEUR_UNITE_LEGALE = 'caractereEmployeurUniteLegale'
    CHANGEMENT_CARACTERE_EMPLOYEUR_UNITE_LEGALE = 'changementCaractereEmployeurUniteLegale'
    CHANGEMENT_DENOMINATION_USUELLE_UNITE_LEGALE = 'changementDenominationUsuelleUniteLegale'


class LegalUnitsEnum(enum.Enum):
    SCORE = 'score'
    SIREN = 'siren'
    STATUT_DIFFUSION_UNITE_LEGALE = 'statutDiffusionUniteLegale'
    UNITE_PURGEE_UNITE_LEGALE = 'unitePurgeeUniteLegale'
    DATE_CREATION_UNITE_LEGALE = 'dateCreationUniteLegale'
    DATE_NAISSANCE_UNITE_LEGALE = 'dateNaissanceUniteLegale'
    CODE_COMMUNE_NAISSANCE_UNITE_LEGALE = 'codeCommuneNaissanceUniteLegale'
    CODE_PAYS_NAISSANCE_UNITE_LEGALE = 'codePaysNaissanceUniteLegale'
    LIBELLE_NATIONALITE_UNITE_LEGALE = 'libelleNationaliteUniteLegale'
    IDENTIFIANT_ASSOCIATION_UNITE_LEGALE = 'identifiantAssociationUniteLegale'
    TRANCHE_EFFECTIFS_UNITE_LEGALE = 'trancheEffectifsUniteLegale'
    ANNEE_EFFECTIFS_UNITE_LEGALE = 'anneeEffectifsUniteLegale'
    DATE_DERNIER_TRAITEMENT_UNITE_LEGALE = 'dateDernierTraitementUniteLegale'
    NOMBRE_PERIODES_UNITE_LEGALE = 'nombrePeriodesUniteLegale'
    CATEGORIE_ENTREPRISE = 'categorieEntreprise'
    ANNEE_CATEGORIE_ENTREPRISE = 'anneeCategorieEntreprise'
    SIGLE_UNITE_LEGALE = 'sigleUniteLegale'
    SEXE_UNITE_LEGALE = 'sexeUniteLegale'
    PRENOM_1_UNITE_LEGALE = 'prenom1UniteLegale'
    PRENOM_2_UNITE_LEGALE = 'prenom2UniteLegale'
    PRENOM_3_UNITE_LEGALE = 'prenom3UniteLegale'
    PRENOM_4_UNITE_LEGALE = 'prenom4UniteLegale'
    PRENOM_USUEL_UNITE_LEGALE = 'prenomUsuelUniteLegale'
    PSEUDONYME_UNITE_LEGALE = 'pseudonymeUniteLegale'
    ACTIVITE_PRINCIPALE_NAF_25_UNITE_LEGALE = 'activitePrincipaleNAF25UniteLegale'
