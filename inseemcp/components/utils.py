import json
from collections.abc import Sequence

import pandas
import pydantic

from models.base import LegalUnitModel


def dataframe_to_models(df: pandas.DataFrame) -> list[LegalUnitModel]:
    json_data = json.loads(df.to_json(orient='records'))
    return [LegalUnitModel(**item) for item in json_data]


class PaginationInfo(pydantic.BaseModel):
    """Information about the pagination of a list of items.
    
    Attributes:
        limit (int): The maximum number of items per page.
        offset (int): The index of the first item in the current page.
        total (int): The total number of items across all pages.
        number_of_pages (int): The total number of pages available.
    """
    limit: int
    offset: int
    total: int
    number_of_pages: int


def paginate[T = LegalUnitModel](limit: int = 100, offset: int = 0, values: Sequence[T] = ()) -> tuple[list[T], PaginationInfo]:
    limit = min(limit, 100)
    offset = min(offset, len(values))

    pagination_info = PaginationInfo(
        limit=limit, 
        offset=offset, 
        total=len(values), 
        number_of_pages=(len(values) + limit - 1) // limit
    )
    return values[offset:offset + limit], pagination_info
