import pydantic


class AverageAgeModel(pydantic.BaseModel):
    """Represents the average age of elected officials.
    
    Attributes:
        total_count (int): The total number of elected officials.   
        average (float): The average age of elected officials.
    """
    total_count: int | None = None
    average: float | None = None
