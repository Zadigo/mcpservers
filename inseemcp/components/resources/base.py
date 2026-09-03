from fastmcp.resources import FileResource, ResourceContent, ResourceResult, resource

from utils import BASE_DIR

RESOURCE_DIR = BASE_DIR / 'components' / 'resources' / 'data'

@resource("dataset://description")
def dataset_description():
    return ResourceResult(
        contents=[
            ResourceContent(
                content=FileResource(
                    title='Dataset Description',
                    description='A detailed description of the dataset and column definitions.',
                    path=str(RESOURCE_DIR / 'description.md'),
                    uri=RESOURCE_DIR.joinpath('description.md').as_uri(),
                )
            ),
            ResourceContent(
                content=FileResource(
                    title='NAF Codes',
                    description='List of NAF codes with their corresponding descriptions.',
                    path=str(RESOURCE_DIR / 'naf.csv'),
                    uri=RESOURCE_DIR.joinpath('naf.csv').as_uri(),
                    mime_type='text/csv',
                    tags={'naf', 'code', 'description'}
                )
            )
        ]
    )
