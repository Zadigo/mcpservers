from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.base import AbstractRequester
    from backend.operators import And, Inversion, Or, Period, To, WildCard
    from backend.requests import BaseRequest


type TypeAbstractRequester = AbstractRequester

type TypeBaseRequest = BaseRequest

type TypeCondition = And | Or | To | Period | WildCard | Inversion
