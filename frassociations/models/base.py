import pydantic


class FileInfo(pydantic.BaseModel):
    """
    FileInfo is a Pydantic model that represents information about a file.
    It includes attributes such as the file's name, size, and type.
    """
    
    name: str
    path: str
