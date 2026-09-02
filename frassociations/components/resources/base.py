import aiofiles
from fastmcp.resources import ResourceContent, ResourceResult, resource

from components.utils import dataframe_to_models
from utils import BASE_DIR, FilesQueryset


@resource('dataset://french-associations')
async def association_resource_dataset():
    """Returns a dataset of French associations."""
    instance = FilesQueryset()

    df = await instance.prefetch_files()
    # payload = df.to_json(orient='records')

    return ResourceResult(
        contents=[
            ResourceContent(
                content=dataframe_to_models(df),
                meta={
                    "title": "French Associations Dataset",
                    "description": "Dataset of French associations, provided by the Répertoire National des Associations.",
                    "source": "https://www.data.gouv.fr/datasets/repertoire-national-des-associations",
                    "format": "JSON",
                    "size": len(df),
                }
            )
        ]
    )


@resource('dataset://french-associations/description')
async def dataset_description():
    path = BASE_DIR.joinpath('components', 'resources', 'templates', 'description.md')
    async with aiofiles.open(path, mode='r') as f:
        description = await f.read()
        return ResourceResult(
            contents=[
                ResourceContent(
                    content=description,
                    meta={
                        "title": "French Associations Dataset Description",
                        "description": "Description of the French associations dataset.",
                        "source": "https://www.data.gouv.fr/datasets/repertoire-national-des-associations",
                        "format": "Markdown",
                    }
                )
            ]
        )
