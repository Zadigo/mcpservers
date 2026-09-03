import pathlib

import dotenv

BASE_DIR = pathlib.Path(__file__).parent.absolute()

dotenv.load_dotenv(BASE_DIR / ".env")

class Requester:
    base_url: str = None


class LegalUnitsRequester(Requester):
    base_url: str = "https://api.insee.fr/entreprises/sirene/V3"
