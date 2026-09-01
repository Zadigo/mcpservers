from fastmcp.tools import tool


@tool
def list_datasets() -> list[str]:
    pass


@tool
def get_dataset(name: str) -> dict:
    pass



@tool
def get_elected_official_in_dataset(name: str, dataset_name: str) -> dict:
    pass
