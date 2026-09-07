
from backend.utils import BaseRequest
from models.university import UniversityModel


class UniversityRequest(BaseRequest):
    base_url = 'https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-principaux-etablissements-enseignement-superieur/exports/json'
    model: type[UniversityModel] = UniversityModel

    def clean(self, data):
        if isinstance(data, list):
            list_values = [
                'siren', 
                'siret', 
                'identifiant_idref', 
                'identifiant_ror', 
                'identifiant_wikidata', 
                'type_d_etablissement'
            ]
            for item in data:
                for key, value in item.items():
                    if key in list_values:
                        item[key] = ','.join(value)
        return data
