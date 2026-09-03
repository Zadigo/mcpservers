# from fastmcp.resources import FileResource, ResourceContent, ResourceResult, resource

# from utils import BASE_DIR

# RESOURCE_DIR = BASE_DIR / 'components' / 'resources' / 'data'

# @resource("dataset://read-me")
# def dataset_description():
#     return ResourceResult(
#         contents=[
#             ResourceContent(
#                 content=FileResource(
#                     title='Dataset Description',
#                     description='A detailed description of the dataset and column definitions.',
#                     path=str(RESOURCE_DIR / 'README.md'),
#                     uri=RESOURCE_DIR.joinpath('README.md').as_uri(),
#                 )
#             ),
#             ResourceContent(
#                 content=FileResource(
#                     title='NAF Codes',
#                     description='List of NAF codes with their corresponding descriptions.',
#                     path=str(RESOURCE_DIR / 'naf.csv'),
#                     uri=RESOURCE_DIR.joinpath('naf.csv').as_uri(),
#                     mime_type='text/csv',
#                     tags={'naf', 'code', 'description'}
#                 )
#             ),
#             ResourceContent(
#                 content=FileResource(
#                     title='Response Tables',
#                     description='Response tables for the dataset.',
#                     path=str(RESOURCE_DIR / 'response_tables.md'),
#                     uri=RESOURCE_DIR.joinpath('response_tables.md').as_uri(),
#                     mime_type='text/markdown',
#                     tags={'response', 'table'}
#                 )
#             )
#         ]
#     )
