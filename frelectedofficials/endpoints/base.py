from __future__ import annotations

import asyncio
import io
import logging
import pathlib
from abc import ABC, abstractmethod
from typing import Any

import httpx2
import pandas
import unidecode

from models.base import FileInfo, RegistryInfo
from utils import MEDIA_DIR, redis_client

logger = logging.getLogger(__name__)

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
                    using=instance.__class__.__name__,
                    created_on=pandas.Timestamp.now(tz='UTC').isoformat()
                )
            )

            async with FILE_WRITER_LOCK:
                await registry.create_file()

        return await instance.get_dataframe()


class ElectedOfficials(ABC):
    """Base class for elected officials. This class provides 
    methods to fetch and process CSV files containing 
    information about elected officials.
    
    Attributes:
        url (str): The URL to fetch the CSV file from.
        fr_title (str): The French title of the elected officials.
        filename (str): The name of the CSV file to save the data to.
    """

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
    def parquet_filepath(self) -> pathlib.Path:
        """Returns the full path to the Parquet file."""
        return self.get_filepath.with_suffix('.parquet')

    @property
    def translation_dict(self) -> dict[str, str]:
        """Use this property to provide a translation dictionary 
        for renaming from their french column names to English."""
        return {}
    
    @abstractmethod
    async def get_dataframe(self) -> pandas.DataFrame | None:
        return await self.fetch_cache_or_csv()
    
    async def fetch_csv_file(self, fetch_only: bool = False, no_fix: bool = False, cache_url: bool = False):
        """Fetches the CSV file from the URL.
        
        Args:
            fetch_only (bool): If True, returns the raw CSV content without processing.
            no_fix (bool): If True, returns the raw DataFrame without renaming columns or calculating additional fields.
            cache_url (bool): If True, caches content of the url in Redis for future use which for example is useful for testing and debugging to avoid repeated network requests.
        """
        url_cache_key = f'urls:{self.filename}'

        db = redis_client()
        if cache_url and db.get(url_cache_key):
            logger.info(f"Using cached URL content for {self.filename}.")
            cached_content = db.get(url_cache_key)
            return pandas.read_csv(io.StringIO(cached_content), sep=';')

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

            if cache_url:
                db.set(
                    url_cache_key,
                    response.content,
                    ex=(15 * 24 * 60 * 60)  # Cache for 15 days
                )

            if response.status_code != 200:
                raise ValueError(f"Failed to fetch CSV file: {response.status_code}")

            if fetch_only:
                return io.BytesIO(response.content)

            buffer = io.BytesIO(response.content)
            self._dataframe = pandas.read_csv(buffer, sep=';')

            if no_fix:
                return self._dataframe

            # Rename the columns to be more Pythonic 
            # (lowercase and underscores instead of spaces)
            old_columns: dict[str, str] = {}
            for column in self._dataframe.columns:
                lowercase = column.lower().replace(' ', '_').replace('-', '_').replace("'", '')
                new_column = unidecode.unidecode(lowercase)  # Remove accents
                old_columns[column] = new_column
            self._dataframe.rename(columns=old_columns, inplace=True)

            # Calculate the age and years_in_office columns based on 
            # the birth_date and mandate_start_date columns
            def calculator(column: str) -> pandas.Series:
                return pandas.to_datetime('today').year - pandas.to_datetime(self._dataframe[column], errors='coerce').dt.year

            self._dataframe['age'] = calculator('date_de_naissance')
            self._dataframe['duree_du_mandat'] = calculator('date_de_debut_du_mandat')

            # Correction for "code_du_departement" which raising
            # an error when saving to parquet: pyarrow.lib.ArrowInvalid: ("Could not convert '27' 
            # with type str: tried to convert to int64", 'Conversion failed for column 
            # code_du_departement with type object')
            # 1. Department codes (2 digits, e.g., '01', '2A')
            if 'code_du_departement' in self._dataframe.columns:
                self._dataframe['code_du_departement'] = self._dataframe['code_du_departement'].astype(str).str.zfill(2)

            # 2. Commune/INSEE codes (5 digits, e.g., '27599', '01001')
            if 'code_de_la_commune' in self._dataframe.columns:
                self._dataframe['code_de_la_commune'] = self._dataframe['code_de_la_commune'].astype(str).str.zfill(5)

            # 3. Postal codes (5 digits, e.g., '75001') - Add this defensively if you have it
            if 'code_postal' in self._dataframe.columns:
                self._dataframe['code_postal'] = self._dataframe['code_postal'].astype(str).str.zfill(5)

            self._dataframe.to_parquet(self.parquet_filepath, index=False)

            # if self.translation_dict:
            #     self._dataframe.rename(columns=self.translation_dict, inplace=True)

            return self._dataframe

    async def fetch_cache_or_csv(self, force_clear_cache: bool = False, **kwargs: Any) -> pandas.DataFrame | None:
        """Fetches the CSV file from the URL or retrieves it from Redis cache if available.
        
        Args:
            force_clear_cache (bool): If True, clears the Redis cache before fetching the data.
        """
        columns_cache_key = self.redis_cache_key.removesuffix(':data') + ':columns'

        logger.info(f"Fetching elected officials data for {self.fr_title} from cache or CSV file.")

        client = redis_client()
        if force_clear_cache:
            client.delete(self.redis_cache_key)
            client.delete(columns_cache_key)

        cached_data = client.get(self.redis_cache_key)

        if cached_data:
            self._dataframe = pandas.read_json(io.StringIO(cached_data), orient='records')
        else:
            # First, try to get the local parquet file if it exists
            filepath = self.get_filepath.with_suffix('.parquet')
            if filepath.exists():
                self._dataframe = pandas.read_parquet(filepath)
            else:
                self._dataframe = await self.fetch_csv_file(**kwargs)

            client.set(
                self.redis_cache_key,
                self._dataframe.to_json(orient='records'),
                ex=(15 * 24 * 60 * 60)  # Cache for 15 days
            )
            client.lpush(
                columns_cache_key,
                *self._dataframe.columns.to_list()
            )
            client.expire(
                columns_cache_key, 
                (15 * 24 * 60 * 60)
            )  # Cache for 15 days

        return self._dataframe


async def generate_elected_officials(creator: AbstractCreator) -> pandas.DataFrame | None:
    """Generates the elected officials data by fetching it from the CSV file or Redis cache.
    Args:
        creator (AbstractCreator): An instance of a class that implements the AbstractCreator interface.
    """
    registry = RegistryInfo(count=0, files=[])
    return await creator.get_elected_official(registry=registry)
