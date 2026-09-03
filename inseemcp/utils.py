import logging
import os
import pathlib
import sys

import dotenv
import redis

BASE_DIR = pathlib.Path(__file__).parent.absolute()

dotenv.load_dotenv(BASE_DIR / ".env")

logging.basicConfig(level=logging.INFO, stream=sys.stderr)

logger = logging.getLogger("freselectedofficials")

def get_redis():
    redis_url = os.getenv("REDIS", "redis://localhost:6379/0")
    client = redis.from_url(redis_url)

    try:
        client.ping()
    except redis.exceptions.ConnectionError:
        raise RuntimeError(f"Could not connect to Redis at {redis_url}")

    return client

class Requester:
    base_url: str = None


class LegalUnitsRequester(Requester):
    base_url: str = "https://api.insee.fr/entreprises/sirene/V3"
