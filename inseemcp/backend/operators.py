from abc import ABC, abstractmethod
from collections.abc import Sequence

from pydantic import BaseModel, Field

from models.base import EstablishmentEnum, LegalUnitEnum


class KeyValuePair(BaseModel):
    """
    Example

    key:value
    """
    key: LegalUnitEnum | EstablishmentEnum = Field(default=LegalUnitEnum.NOM_UNITE_LEGALE)
    value: str | None = Field(default=None)

    def resolve(self):
        if self.value is None:
            self.value = ''
        return f"{self.key.value}:{self.value}"


class BaseCondition(ABC):
    template: str = ''

    def __repr__(self):
        return f'<{self.__class__.__name__}>'
    
    @abstractmethod
    def resolve(self) -> str:
        return self.template

    @staticmethod
    def join_values(values: Sequence[str]):
        return ' '.join(values)

    # def resolve_key_value_pair(self):
    #     if isinstance(self.lhv, KeyValuePair):
    #         return self.lhv.resolve()
    #     return self.lhv
        
    #     # if isinstance(self.lhv, str) and (not self.lhv.endswith('*') or self.lhv.startswith('-')):
    #     #     raise ValueError()


class BaseOperator:
    def __init__(self, lhv: KeyValuePair, rhv: KeyValuePair):
        self.lhv = lhv
        self.rhv = rhv

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.lhv}: {self.rhv}>'

    def resolve(self):
        if isinstance(self.lhv, str) and isinstance(self.rhv, str):
            return self.template.format(
                lhv=self.lhv,
                rhv=self.rhv
            )
        
        return self.template.format(
            lhv=self.lhv.resolve(), 
            rhv=self.rhv.resolve()
        )


class And(BaseOperator, BaseCondition):
    template: str = '{lhv} AND {rhv}'


class Or(BaseOperator, BaseCondition):
    template: str = '{lhv} OR {rhv}'


class To(BaseCondition):
    template: str = '{lhv} TO {rhv}'

    def __init__(self, column: LegalUnitEnum, lhv: str, rhv: str):
        self.column = column
        self.lhv = lhv
        self.rhv = rhv

    def resolve(self):
        return self.template.format(
            lhv=self.lhv.resolve(), 
            rhv=self.rhv.resolve()
        )


class Period(BaseCondition):
    template: str = 'periode({values})'

    def __init__(self, *values: And | Or):
        self.values = values
    
    def resolve(self):
        str_values = self.join_values(value.resolve() for value in self.values)
        return self.template.format(values=str_values)


class Inversion(BaseCondition):
    """Inverts a KeyValuePair by prepending a minus sign.

    .. code-block:: python

        # -nomUniteLegale:test
        kv = KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='test')
        inverted = Inversion(kv)
    """

    template: str = '-{lhv}'

    def __init__(self, lhv: KeyValuePair):
        self.lhv = lhv
        
    def resolve(self):
        result = self.lhv.resolve()
        if result.startswith('-'):
            return result
        return self.template.format(lhv=result)


class WildCard(BaseCondition):
    """
    This is a wildcard condition for a KeyValuePair,
    appending an asterisk `*` to its resolved value. It can be inverted
    using the `~` operator.

    To check that a value starts with::

        # numUniteLegale:test*
        WildCard(KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='test'))

    To check that it contains a value:

        # numUniteLegale:*
        WildCard(KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value=None))

    To check that it does not contain a value::

        # -numUniteLegale:*
        ~WildCard(KeyValuePair(key=LegalUnitEnum.NOM_UNITE_LEGALE, value='test'))
        
    """

    template: str = '{value}*'

    def __init__(self, value: KeyValuePair):
        self.value = value

    def __invert__(self):
        inversion = Inversion(self.value).resolve()
        return self.template.format(value=inversion)

    def resolve(self):
        return self.template.format(value=self.value.resolve())
