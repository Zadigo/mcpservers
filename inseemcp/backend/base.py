from abc import ABC, abstractmethod
from typing import Any
from urllib.parse import urlencode

import httpx2

from backend.models import StartsWithQuery


class AbstractRequester(ABC):
    version: float = 3.11
    base_url: str = 'https://api.insee.fr/api-sirene/{version}/'

    @abstractmethod
    def get_url(self, **kwargs: Any):
        return self.base_url.format(version=self.version, **kwargs)

    async def request(self):
        async with httpx2.AsyncClient() as client:
            response = await client.get(self.get_url())
            response.raise_for_status()
            return response.json()


class Siren(AbstractRequester):
    base_url: str = 'https://api.insee.fr/api-sirene/{version}/{siren}'

    def get_url(self, siren: str):
        return super().get_url(siren=siren)


class Siret(AbstractRequester):
    """
    
    ## Examples

    Recherche de tous les établissement dont le siren commence par 3:

    .. code-block:: markdown

        https://api.insee.fr/api-sirene/3.11/siret?q=siren:3*&champs=siret,denominationUniteLegale&curseur=*


    """
    base_url: str = 'https://api.insee.fr/api-sirene/{version}/{siret}'
    
    def get_url(self, siret: str):
        return super().get_url(siret=siret)
    

class AbstractMultiSearch(AbstractRequester):
    def search_all(self, value: int):
        """
        Recherche de tous les établissements du Siren 775672272 :

            https://api.insee.fr/api-sirene/3.11/siret?q=siren:775672272
        """
        return urlencode({'q': f'siren:{value}'})

    def start_with(self, query: StartsWithQuery):
        return urlencode({
            'q': f'siren:{query.q}*',
            'champs': ','.join(query.champs),
            'curseur': query.curseur
        })


class MultiSearchSiren(AbstractMultiSearch):
    base_url: str = 'https://api.insee.fr/api-sirene/3.11/siren?q={query}'

    def get_url(self, **kwargs: Any):
        query_string = urlencode(kwargs)
        return self.base_url.format(query=query_string)


class MultiSearchSiret(AbstractMultiSearch):
    base_url: str = 'https://api.insee.fr/api-sirene/3.11/siret?q={query}'

    def get_url(self, **kwargs: Any):
        query_string = urlencode(kwargs)
        return self.base_url.format(query=query_string)
