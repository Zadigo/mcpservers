import aiofiles
from fastmcp.resources import ResourceContent, ResourceResult, resource

from components.utils import dataframe_to_models, paginate
from utils import BASE_DIR, FilesQueryset


@resource('dataset://french-associations')
async def association_resource_dataset():
    """Returns a dataset of French associations."""
    instance = FilesQueryset()

    df = await instance.prefetch_files()
    values = dataframe_to_models(df)
    # payload = df.to_json(orient='records')

    return ResourceResult(
        contents=[
            ResourceContent(
                content=paginate(limit=100, offset=0, values=values),
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


@resource('dataset://french-associations/count-by-region')
async def count_by_region():
    """
    Count the number of associations by region.
    
    Returns:
        dict: A dictionary with regions as keys and counts as values.
    """
    instance = FilesQueryset()
    df = await instance.prefetch_files()

    # Group by region and count
    df = df[~df['adrs_libcommune'].isna()]
    region_counts = df.groupby('adrs_libcommune').size().to_dict()

    return ResourceResult(
        contents=[
            ResourceContent(
                content=region_counts,
                meta={
                    "title": "Count of Associations by Region",
                    "description": "Counts the number of associations in each region.",
                    "source": "https://www.data.gouv.fr/datasets/repertoire-national-des-associations",
                    "format": "JSON",
                }
            )
        ]
    )
