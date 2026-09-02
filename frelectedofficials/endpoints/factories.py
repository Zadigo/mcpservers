from __future__ import annotations

import pandas

from endpoints.base import ElectedOfficials


class DistrictCouncillor(ElectedOfficials):
    """Concrete implementation of the ElectedOfficials class for District Councillor elected officials."""

    url: str = 'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-154541/elus-conseiller-darrondissement-ca.csv'
    filename: str = 'elus-conseiller-darrondissement-ca.csv'
    fr_title: str = "Élus Conseiller d'Arrondissement"

    @property
    def translation_dict(self) -> dict[str, str]:
        return {
            'code_du_departement': 'department_code',
            'libelle_du_departement': 'department_name',
            'code_de_la_commune': 'commune_code',
            'libelle_de_la_commune': 'commune_name',
            'libelle_du_secteur': 'sector_name',
            'prenom_de_lelu': 'first_name',
            'nom_de_lelu': 'last_name',
            'code_sexe': 'gender_code',
            'date_de_naissance': 'birth_date',
            'code_de_la_categorie_socio_professionnelle': 'socio_professional_category_code',
            'libelle_de_la_categorie_socio_professionnelle': 'socio_professional_category_name',
            'date_de_debut_du_mandat': 'mandate_start_date',
            'libelle_de_la_fonction': 'function_name',
            'date_de_debut_de_la_fonction': 'function_start_date',
            'age': 'age',
            'duree_du_mandat': 'years_in_office'
        }

    async def get_dataframe(self) -> pandas.DataFrame | None:
        return await super().get_dataframe()


