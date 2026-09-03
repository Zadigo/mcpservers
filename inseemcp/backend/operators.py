from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

from models.base import LegalUnitEnum


class KeyValuePair(BaseModel):
    """
    Example

    key:value
    """
    key: LegalUnitEnum = Field(default=LegalUnitEnum.NOM_UNITE_LEGALE)
    value: str = Field(default=None)

    def resolve(self):
        return f"{self.key.value}:{self.value}"


class BaseOperator(ABC):
    CONDITION_AND: str =  '{lhv} AND {rhv}'
    CONDITION_OR: str = '{lhv} OR {rhv}'
    PERIOD: str = 'period{values}'

    def __init__(self, lhv: str, rhv: str):
        self.lhv = lhv
        self.rhv = rhv

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.resolve()}>'

    @property
    def operator_name(self):
        return self.__class__.__name__.lower()

    @abstractmethod
    def resolve(self) -> str | KeyValuePair:
        return ''


class And(BaseOperator):
    """
    Recherche de tous les établissements qui ont au moins une période où leur état est « actif » et leur activité principale est 84.23Z :
    ?q=periode(activitePrincipaleEtablissement:84.23Z AND etatAdministratifEtablissement:A)

    Recherche de tous les établissements qui ont moins une période dont l'activitePrincipaleEtablissement est 84.23Z et qui n'ont jamais été fermés :
    ?q=periode(activitePrincipaleEtablissement:84.23Z) AND -periode(etatAdministratifEtablissement:F)

    Recherche de tous les établissements de Malakoff dont la dernière catégorie juridique est 9220 :
    ?q=codeCommuneEtablissement:92046 AND categorieJuridiqueUniteLegale:9220

    Recherche de toutes les entreprises exerçant l'activité « marchand de biens » et appartenant à la catégorie PME (Cf. supra : combinaison de variables historisées et non-historisées, paramètre date) :
    ?q=periode(activitePrincipaleUniteLegale:68.10Z) AND categorieEntreprise:PME&date=2030-12-31
    """

    def resolve(self):
        return self.CONDITION_AND.format(lhv=self.lhv, rhv=self.rhv)


class Or(BaseOperator):
    """
    Recherche de toutes les entreprises dont l'activité principale est 84.23Z ou 86.21Z, ou l'a été par le passé :
    ?q=periode(activitePrincipaleUniteLegale:84.23Z OR activitePrincipaleUniteLegale:86.21Z)

    Recherche de tous les établissements relevant des catégories juridiques 5510 et 5520 :
    ?q=categorieJuridiqueUniteLegale:5510 OR categorieJuridiqueUniteLegale:5520
    """

    def resolve(self):
        return self.CONDITION_OR.format(lhv=self.lhv, rhv=self.rhv)


class To(BaseOperator):
    """
    Recherche de tous les etablissements d'UL dont le nom d'usage va de DUPONT à DURAND, y compris DUPONT et DURAND :

    .. code-block text::
        ?q=nomUsageUniteLegale:[DUPONT TO DURAND]
    """
    def __init__(self, column: LegalUnitEnum, lhv: str, rhv: str):
        self.column = column
        self.lhv = lhv
        self.rhv = rhv

    def resolve(self):
        value = f'[{self.lhv} TO {self.rhv}]'
        return KeyValuePair(key=self.column.value, value=value)


class Period(BaseOperator):
    def __init__(self, *values: And | Or):
        self.values = values

    def resolve(self):
        str_values = [value.resolve() for value in self.values]
        return self.PERIOD.format(values=str_values)
