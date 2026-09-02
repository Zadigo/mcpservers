import json

import pandas

from models.results import AssociationModel


def dataframe_to_models(df: pandas.DataFrame):
    json_data = json.loads(df.to_json(orient='records'))
    return [AssociationModel(**item) for item in json_data]
