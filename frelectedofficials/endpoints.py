from __future__ import annotations

import asyncio
import io
import pathlib
from abc import ABC, abstractmethod

import httpx2
import pandas
import unidecode

from models.base import FileInfo, RegistryInfo
from utils import MEDIA_DIR, redis_client

FILE_WRITER_LOCK = asyncio.Lock()


class AbstractCreator(ABC):
    @abstractmethod
    def factory_method(self) -> ElectedOfficials:
        pass

    async def get_elected_official(self, registry: RegistryInfo | None = None) -> pandas.DataFrame | None:
        instance = self.factory_method()

        if registry is not None:
            registry.count += 1

            registry.files.append(
                FileInfo(
                    title=instance.fr_title,
                    filepath=str(instance.get_filepath),
                    created_on=pandas.Timestamp.now(tz='UTC').isoformat()
                )
            )

            async with FILE_WRITER_LOCK:
                await registry.create_file()

        return await instance.get_dataframe()


class ConcreteDistrictCouncillor(AbstractCreator):
    def factory_method(self) -> ElectedOfficials:
        instance = DistrictCouncillor()
        return instance


class ElectedOfficials(ABC):
    url: str = ''
    fr_title: str = ''
    filename: str = ''

    def __init__(self):
        self._dataframe: pandas.DataFrame | None = None

        if self.filename == '':
            raise ValueError("Filename is not set for the elected officials class.")

        self.redis_cache_key: str = f'{self.filename}:data'

    def __repr__(self):
        return f"<ElectedOfficials: {self.fr_title}>"

    @property
    def get_filepath(self) -> pathlib.Path:
        """Returns the full path to the CSV file."""
        return MEDIA_DIR.joinpath(self.filename)

    @property
    def translation_dict(self) -> dict[str, str]:
        """Use this property to provide a translation dictionary 
        for renaming from their french column names to English."""
        return {}
    
    @abstractmethod
    async def get_dataframe(self) -> pandas.DataFrame | None:
        return await self.fetch_cache_or_csv()
    
    async def fetch_csv_file(self):
        """Fetches the CSV file from the URL."""
        if self.url == '' or self.url is None:
            raise ValueError("URL is not set for the elected officials class.")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept': 'text/csv',
            'Content-Type': 'text/csv',
        }

        async with httpx2.AsyncClient() as client:
            response = await client.get(self.url, headers=headers)
            response.raise_for_status()

            if response.status_code != 200:
                raise ValueError(f"Failed to fetch CSV file: {response.status_code}")

            buffer = io.BytesIO(response.content)
            self._dataframe = pandas.read_csv(buffer, sep=';')

            # Rename the columns to be more Pythonic 
            # (lowercase and underscores instead of spaces)
            old_columns: dict[str, str] = {}
            for column in self._dataframe.columns:
                lowercase = column.lower().replace(' ', '_').replace('-', '_').replace("'", '')
                new_column = unidecode.unidecode(lowercase)  # Remove accents
                old_columns[column] = new_column

            self._dataframe.rename(columns=old_columns, inplace=True)
            self._dataframe.to_parquet(MEDIA_DIR / self.filename.replace('.csv', '.parquet'), index=False)

            if self.translation_dict:
                self._dataframe.rename(columns=self.translation_dict, inplace=True)

            return self._dataframe

    async def fetch_cache_or_csv(self):
        """Fetches the CSV file from the URL or retrieves it from Redis cache if available."""
        client = redis_client()
        cached_data = client.get(self.redis_cache_key)

        if cached_data:
            self._dataframe = pandas.read_csv(io.StringIO(cached_data), sep=';')
        else:
            self._dataframe = await self.fetch_csv_file()
            client.set(
                self.redis_cache_key,
                self._dataframe.to_csv(index=False, sep=';'),
                ex=(15 * 24 * 60 * 60)  # Cache for 15 days
            )

        return self._dataframe


class DistrictCouncillor(ElectedOfficials):
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


async def generate_elected_officials(creator: AbstractCreator) -> pandas.DataFrame | None:
    """Generates the elected officials data by fetching it from the CSV file or Redis cache.
    Args:
        creator (AbstractCreator): An instance of a class that implements the AbstractCreator interface.
    """
    # registry = JsonRegistry(count=1, files=[])
    registry = RegistryInfo(count=1, files=[])
    return await creator.get_elected_official(registry=registry)
