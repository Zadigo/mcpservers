from typing import Literal

from fastmcp.resources import ResourceContent, ResourceResult, resource

from constants import ESTABLISHMENT_FIELDS, LEGAL_UNITS_FIELDS


@resource("dataset://available-columns/{entity}")
def available_columns(entity: Literal['legal units', 'establishments']):
    """Returns a list of all the available columns used by the INSEE SIERENE dataset.
    It describes two different types of entities: legal units and establishments."""
    content = LEGAL_UNITS_FIELDS if entity == 'legal units' else ESTABLISHMENT_FIELDS
    return ResourceResult(
        contents=[
            ResourceContent(
                content=content
            )
        ]
    )
