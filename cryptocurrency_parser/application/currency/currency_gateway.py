from abc import abstractmethod
from typing import Protocol

from domain.models.currency.currency import Currency
from domain.models.currency.currency_id import CurrencyId


class CurrencyReader(Protocol):
    @abstractmethod
    async def get_currency_by_id(
        self,
        currency_id: CurrencyId,
    ) -> Currency | None:
        raise NotImplementedError

    @abstractmethod
    async def get_currency_by_ticker(
        self,
        currency_ticker: str,
    ) -> Currency | None:
        raise NotImplementedError


class CurrencyAdder(Protocol):
    @abstractmethod
    async def save_currency(self, currency: Currency) -> None:
        raise NotImplementedError


class CurrencyRemover(Protocol):
    @abstractmethod
    async def remove_currency_by_id(self, currency_id: CurrencyId) -> None:
        raise NotImplementedError

    @abstractmethod
    async def remove_currency_by_ticker(self, currency_ticker: str) -> None:
        raise NotImplementedError
