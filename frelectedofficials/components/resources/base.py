import json

import aiofiles
from fastmcp.exceptions import ResourceError
from fastmcp.resources import (
    ResourceContent,
    ResourceResult,
    resource,
)

from models.base import get_registry
from models.results import DistrictCouncillorEN
from utils import BASE_DIR


@resource('file:///components/resources/templates/data-gouv.md')
async def global_dataset_information():
    """Get information about the global datasets."""
    fullpath = BASE_DIR / 'components/resources/templates/data-gouv.md'

    try:
        async with aiofiles.open(fullpath, mode="r") as f:
            content = await f.read()
        return content
    except FileNotFoundError:
        return "Resource not found: data-gouv.md"


@resource("dataset://elus-conseiller-darrondissement")
def get_district_councillors_dataset() -> ResourceResult:
    """Get the dataset of district councilors as a downloadable resource.

    Exposes the full dataset (all records) as JSON, without injecting it
    into the LLM's conversational context — meant for on-demand retrieval
    by the client, not for use as a Tool result.
    """
    name = "Élus Conseiller d'Arrondissement"
    result = get_registry().get_file_by_title(name)

    if result is None:
        raise ResourceError(
            f"Dataset '{name}' not found. Available datasets: {get_registry().str_filetitles}"
        )

    records = [
        DistrictCouncillorEN(**row)
        for row in result.get_content_as_json()
    ]

    payload = json.dumps(
        [record.model_dump(mode="json") for record in records],
        ensure_ascii=False,
    )

    return ResourceResult(
        contents=[
            ResourceContent(
                content=payload,
                mime_type="application/json",
                meta={
                    "title": name,
                    "description": "Dataset of district councilors in France, provided by the Répertoire National des Élus.",
                    "source": "https://www.data.gouv.fr/datasets/repertoire-national-des-elus-1",
                    "format": "JSON",
                    "size": len(records),
                }
            )
        ]
    )
