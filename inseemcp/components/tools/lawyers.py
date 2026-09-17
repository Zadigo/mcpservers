import json
import pathlib
from collections.abc import Sequence

import pandas
from fastmcp.tools import tool

from models.lawyers import LawyersModel
from utils import DATA_DIR


class FileQueryset:
    file_path: pathlib.Path = DATA_DIR.joinpath('lawyers-cleaned.parquet')

    def __init__(self):
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")
        
    def _iterables(self, df: pandas.DataFrame) -> Sequence[LawyersModel]:
        json_data =  df.to_json(orient='records', force_ascii=False)
        return [LawyersModel(**row) for row in json.loads(json_data)]

    def load_cache(self) -> pandas.DataFrame:
        return pandas.read_parquet(self.file_path)

    def get_by_siret(self, siret: str) -> Sequence[LawyersModel]:
        df = self.load_cache()
        df = df[df.cb_siret_nic == siret]
        return self._iterables(df)

    def get_by_siren(self, siren: str) -> Sequence[LawyersModel]:
        df = self.load_cache()
        df = df[df.cb_siret_siren == siren]
        return self._iterables(df)


@tool
def get_lawyers_by_siret(siret: str) -> Sequence[LawyersModel]:
    """
    This is a supporting tool which role is to add additional context to the
    main establishment and legal unit tools.

    Use this tool when a search is successful and when the NAF of the establishment 
    indicates a legal context where lawyers might be relevant. The NAF for legal
    activities is "69.10Z".

    Args:
        siret: The SIRET of the establishment to search for.

    Returns:
        A collection of matching lawyer records associated with the specified SIRET.

    Notes:
        - This tool is intended to provide additional context for establishments
          operating in a legal context.
        - The NAF code "69.10Z" corresponds to legal activities.
    """
    return FileQueryset().get_by_siret(siret)


@tool
def get_lawyers_by_siren(siren: str) -> Sequence[LawyersModel]:
    """
    This is a supporting tool which role is to add additional context to the
    main establishment and legal unit tools.

    Use this tool when a search is successful and when the NAF of the establishment 
    indicates a legal context where lawyers might be relevant. The NAF for legal
    activities is "69.10Z".

    Args:
        siren: The SIREN of the legal unit to search for.

    Returns:
        A collection of matching lawyer records associated with the specified SIREN.

    Notes:
        - This tool is intended to provide additional context for establishments
          operating in a legal context.
        - The NAF code "69.10Z" corresponds to legal activities.
    """
    return FileQueryset().get_by_siren(siren)
