from application.common.exceptions import (
    ApplicationError,
)
from domain.models.currency.currency_id import CurrencyId

type UserIdentifier = str | CurrencyId


class CurrencyNotFoundError(ApplicationError):
    def __init__(
        self,
        identifier: UserIdentifier,
    ) -> None:
        self._identifier = identifier


class CurrencyNotFoundByIdError(CurrencyNotFoundError):
    def __str__(self) -> str:
        return f"Currency with id <{self._identifier}> not found"


class CurrencyNotFoundByTickerError(CurrencyNotFoundError):
    def __str__(self) -> str:
        return f"Currency with ticker <{self._identifier}> not found"


class CurrencyTickerAlreadyInDatabaseError(ApplicationError):
    def __init__(self, ticker: str) -> None:
        self._ticker = ticker

    def __str__(self) -> str:
        return f"Currency with ticker <{self._ticker}> already exists"
