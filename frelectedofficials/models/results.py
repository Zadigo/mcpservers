import pydantic


class DatasetResponseModel(pydantic.BaseModel):
    total: int = 0
    limit: int = 10
    offset: int = 0
    results: list[dict] = []



class BaseInfo(pydantic.BaseModel):
    """Represents the base information about an elected official.
    
    Attributes:
        nom_de_lelu (str): The last name of the elected official.
        prenom_de_lelu (str): The first name of the elected official.
        code_sexe (str): The gender code of the elected official.
        date_de_naissance (str): The birth date of the elected official.
        date_de_debut_du_mandat (str): The start date of the mandate.
        code_du_departement (int): The department code.
        date_de_debut_de_la_fonction (str): The start date of the function.
        libelle_de_la_fonction (str): The function name.
        libelle_de_la_categorie_socio_professionnelle (str): The name of the socio-professional category.
        code_de_la_categorie_socio_professionnelle (int): The socio-professional category code.
    """
    nom_de_lelu: str | None = None
    prenom_de_lelu: str | None = None
    code_sexe: str | None = None
    date_de_naissance: str | None = None
    date_de_debut_du_mandat: str | None = None
    code_du_departement: int | None = None
    date_de_debut_de_la_fonction: str | None = None
    libelle_de_la_fonction: str | None = None
    libelle_de_la_categorie_socio_professionnelle: str | None = None
    code_de_la_categorie_socio_professionnelle: int | None = None
    libelle_du_departement: str | None = None


class AdditionalInfo(pydantic.BaseModel):
    """Represents additional information about an elected official.
    
    Attributes:
        age (int): The age of the elected official.
        years_in_office (int): The number of years the elected official has been in office.
    """
    age: int | None = None
    years_in_office: int | None = None


class DistrictCouncillorFR(AdditionalInfo, BaseInfo, pydantic.BaseModel):
    """Represents an elected official with various attributes.
    
    Attributes:
        libelle_du_departement (str): The name of the department.
        code_de_la_commune (int): The commune code.
        libelle_de_la_commune (str): The name of the commune.
        libelle_du_secteur (str): The sector name.
    """
    libelle_de_la_commune: str | None = None
    code_de_la_commune: int | None = None
    libelle_du_secteur: str | None = None


class MunicipalCouncillorFR(DistrictCouncillorFR):
    """Represents a municipal councillor with various attributes."""

    libelle_de_la_commune: None = pydantic.Field(default=None, exclude=True, repr=False)
    code_de_la_commune: None = pydantic.Field(default=None, exclude=True, repr=False)
    libelle_du_secteur: None = pydantic.Field(default=None, exclude=True, repr=False)
    code_de_la_collectivite_a_statut_particulier: str = None
    libelle_de_la_collectivite_a_statut_particulier: str | None = None


# class DistrictCouncillorEN(AdditionalInfo, pydantic.BaseModel):
#     """Represents an elected official with various attributes in English.
    
#     Attributes:
#         department_code (int): The department code.
#         department_name (str): The name of the department.
#         commune_code (int): The commune code.
#         commune_name (str): The name of the commune.
#         sector_name (str): The sector name.
#         first_name (str): The first name of the elected official.
#         gender_code (str): The gender code of the elected official.
#         birth_date (str): The birth date of the elected official.
#         socio_professional_category_code (int): The socio-professional category code.
#         socio_professional_category_name (str): The name of the socio-professional category.
#         mandate_start_date (str): The start date of the mandate.
#         function_name (str): The function name.
#         function_start_date (str): The start date of the function.
#         age (int): The age of the elected official.
#         years_in_office (int): The number of years in office.
#     """
#     department_code: int | None = None
#     department_name: str | None = None
#     commune_code: int | None = None
#     commune_name: str | None = None
#     sector_name: str | None = None
#     first_name: str | None = None
#     gender_code: str | None = None
#     birth_date: str | None = None
#     socio_professional_category_code: int | None = None
#     socio_professional_category_name: str | None = None
#     mandate_start_date: str | None = None
#     function_name: str | None = None
#     function_start_date: str | None = None

