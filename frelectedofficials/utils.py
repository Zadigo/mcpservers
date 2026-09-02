import json
import pathlib

import dotenv
import pandas
import redis

dotenv.load_dotenv('.env')

BASE_DIR = pathlib.Path(__file__).parent.absolute()


MEDIA_DIR = BASE_DIR / 'media'


REGISTRY = MEDIA_DIR / 'registry.json'


REDIS_CACHE_KEY = 'frelectedofficials:data'


def redis_client():
    client = redis.Redis(
        host='localhost',
        port=6379,
        db=0,
        decode_responses=True
    )

    try:
        client.ping()
    except redis.exceptions.ConnectionError:
        raise ConnectionError(
            "Could not connect to Redis. Please ensure that the Redis server is running.")

    return client


def df_to_json(df: pandas.DataFrame) -> list[dict]:
    return json.loads(df.to_json(orient='records', force_ascii=False))


def to_lowercase(value: str | None):
    if value is None:
        return value
    return value.lower()
