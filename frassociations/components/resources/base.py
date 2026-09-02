from fastmcp.resources import ResourceContent, ResourceResult, resource
    
from utils import FilesQueryset


@resource('dataset://french-associations')
async def association_resource_dataset():
    """Returns a dataset of French associations."""
    instance = FilesQueryset()

    df = await instance.prefetch_files()
    payload = df.to_json(orient='records')

    return ResourceResult(
        contents=[
            ResourceContent(
                content=payload,
                mime_type="application/json",
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
