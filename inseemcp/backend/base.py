
from typing import Any

from backend.utils import BaseRequest
from models.bodacc import BodaccModel
from models.university import UniversityModel


class UniversityRequest(BaseRequest[UniversityModel]):
    """A request that adds additional context to a main search for a
    SIREN or SIRET with the INSEE database."""
    
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
                'type_d_etablissement',
                'rna',
                'anciens_codes_uai'
            ]
            for item in data:
                for key, value in item.items():
                    if key in list_values:
                        if value is None:
                            continue

                        if not isinstance(value, list):
                            continue

                        item[key] = ','.join(value)

                    if key.startswith('inscrits_'):
                        if value is None:
                            continue

                        if isinstance(value, str):
                            try:
                                item[key] = int(value)
                            except (ValueError, TypeError):
                                continue

                    if key == 'coordonnees' and isinstance(value, dict):
                            item[key] = ','.join([str(v) for v in value.values()])
        return data



class BodaccRequest(BaseRequest[BodaccModel]):
    """A request that adds additional context to a main search for a
    Bodacc entry with the INSEE database."""

    base_url = 'https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records'
    model: type[BodaccModel] = BodaccModel

    def clean(self, data) -> list[dict[str, Any]]:
        if data is not None and isinstance(data, dict):
            return data['results']
        return []
