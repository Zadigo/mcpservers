import asyncio
import io
import logging
import os
import pathlib
import sys
from pathlib import Path

import aiofiles
import pandas
import redis
from dotenv import load_dotenv

import models

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger("freselectedofficials")

CACHE_KEY = "frassociations"

BASE_DIR = Path(__file__).parent.absolute()

load_dotenv(BASE_DIR / ".env")


def get_redis():
    redis_url = os.getenv("REDIS", "redis://localhost:6379/0")
    client = redis.from_url(redis_url)

    try:
        client.ping()
    except redis.exceptions.ConnectionError:
        raise RuntimeError(f"Could not connect to Redis at {redis_url}")

    return client


class FilesQueryset:
    def __init__(self):
        self.source = pathlib.Path(os.getenv("SOURCE"))
        if not self.source.exists() and not self.source.is_dir():
            raise RuntimeError(f"Source directory {self.source} does not exist")
        self.files: list[models.FileInfo] = []
        self.cache_files_key: str = CACHE_KEY + ':files'
        self.cache_data_key:str = CACHE_KEY + ':data'

        self.column_types = {
            'adrs_repetition': 'str',
            'adrs_codeinsee': 'str',
            'adrg_codepostal': 'str',
            'id_ex': 'str',
            'siret': 'str',
            'rup_mi': 'str',
        }

    def __repr__(self):
        self.load_cache()
        return f"<FilesQueryset [{len(self.files)}]>"

    def __iter__(self):
        self.load_cache()
        return iter(self.files)
    
    def load_cache(self):
        db = get_redis()
        cache_count = db.scard(self.cache_files_key)
        if cache_count > 0:
            values = db.smembers(self.cache_files_key)
            json_values = [eval(value.decode('utf-8')) for value in values]
            self.files = [models.FileInfo(name=json_value['name'], path=json_value['path']) for json_value in json_values]
            return self.files

        files = list(self.source.iterdir())
        for file in files:
            if file.is_file():
                self.files.append(models.FileInfo(name=file.name, path=file.as_posix()))

        db.sadd(self.cache_files_key, *[str(file.model_dump()) for file in self.files])
        return self.files

    async def prefetch_files(self, limit: int | None = None, clean_cache: bool = False) -> pandas.DataFrame:
        db = get_redis()

        if clean_cache:
            db.delete(self.cache_data_key)
            logger.info("Cache cleared for data")

        self.load_cache()

        db = get_redis()
        dfs: list[pandas.DataFrame] = []

        cache = db.get(self.cache_data_key)
        if cache:
            buffer = io.BytesIO(cache)
            df = pandas.read_json(buffer, orient='records', encoding='utf-8', dtype=self.column_types)
            return df

        async def read_file(fileinfo: models.FileInfo):
            async with aiofiles.open(fileinfo.path, mode='r') as f:
                content = await f.read()
                try:
                    df = pandas.read_csv(io.StringIO(content), sep=';', encoding='utf-8', dtype=self.column_types)
                    logger.info(f"Read file {fileinfo.path} with {df.shape[0]} rows")
                except Exception as e:
                    logger.error(f"Error reading file {fileinfo.path}: {e}")
                else:
                    dfs.append(df)

        tasks: list[asyncio.Task] = []
        for i, file in enumerate(self.files):
            if limit is not None and i >= limit:
                break
            tasks.append(asyncio.create_task(read_file(file)))

        await asyncio.gather(*tasks)

        df = pandas.concat(dfs, ignore_index=True)
        db.set(self.cache_data_key, df.to_json(orient='records', force_ascii=False))

        return df
