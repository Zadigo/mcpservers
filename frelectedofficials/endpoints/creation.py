from endpoints.base import AbstractCreator, ElectedOfficials
from endpoints.factories import DistrictCouncillor


class ConcreteDistrictCouncillor(AbstractCreator):
    """Concrete implementation of the AbstractCreator for District Councillor elected officials.
    This class provides a factory method to create an instance of the DistrictCouncillor class."""

    def factory_method(self) -> ElectedOfficials:
        return DistrictCouncillor()
