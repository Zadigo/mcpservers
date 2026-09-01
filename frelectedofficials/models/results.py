import pydantic


class AdditionalInfo(pydantic.BaseModel):
    """Represents additional information about an elected official.
    
    Attributes:
        age (int): The age of the elected official.
        years_in_office (int): The number of years the elected official has been in office.
    """
    age: int
    years_in_office: int


class DistrictCouncillorFR(AdditionalInfo, pydantic.BaseModel):
    """Represents an elected official with various attributes.
    
    Attributes:
        code_du_departement (int): The department code.
        libelle_du_departement (str): The name of the department.
        code_de_la_commune (int): The commune code.
        libelle_de_la_commune (str): The name of the commune.
        libelle_du_secteur (str): The sector name.
        prenom_de_lelu (str): The first name of the elected official.
        code_sexe (str): The gender code of the elected official.
        date_de_naissance (str): The birth date of the elected official.
        code_de_la_categorie_socio_professionnelle (int): The socio-professional category code.
        libelle_de_la_categorie_socio_professionnelle (str): The name of the socio-professional category.
        date_de_debut_du_mandat (str): The start date of the mandate.
        libelle_de_la_fonction (str): The function name.
        date_de_debut_de_la_fonction (str): The start date of the function
    """
    code_du_departement: int
    libelle_du_departement: str
    code_de_la_commune: int
    libelle_de_la_commune: str
    libelle_du_secteur: str
    prenom_de_lelu: str
    code_sexe: str
    date_de_naissance: str
    code_de_la_categorie_socio_professionnelle: int
    libelle_de_la_categorie_socio_professionnelle: str
    date_de_debut_du_mandat: str
    libelle_de_la_fonction: str
    date_de_debut_de_la_fonction: str


class DistrictCouncillorEN(AdditionalInfo, pydantic.BaseModel):
    """Represents an elected official with various attributes in English.
    
    Attributes:
        department_code (int): The department code.
        department_name (str): The name of the department.
        commune_code (int): The commune code.
        commune_name (str): The name of the commune.
        sector_name (str): The sector name.
        first_name (str): The first name of the elected official.
        gender_code (str): The gender code of the elected official.
        birth_date (str): The birth date of the elected official.
        socio_professional_category_code (int): The socio-professional category code.
        socio_professional_category_name (str): The name of the socio-professional category.
        mandate_start_date (str): The start date of the mandate.
        function_name (str): The function name.
        function_start_date (str): The start date of the function.
        age (int): The age of the elected official.
        years_in_office (int): The number of years in office.
    """
    department_code: int
    department_name: str
    commune_code: int
    commune_name: str
    sector_name: str
    first_name: str
    gender_code: str
    birth_date: str
    socio_professional_category_code: int
    socio_professional_category_name: str
    mandate_start_date: str
    function_name: str
    function_start_date: str
