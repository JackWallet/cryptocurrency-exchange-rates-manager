from abc import abstractmethod
from typing import Protocol
from domain.models.currency.currency_id import CurrencyId
from domain.models.currency.currency import Currency


class CurrencyReader(Protocol):
    @abstractmethod
    async def get_currency(self, currency_id: CurrencyId) -> Currency:
        raise NotImplementedError


class CurrencyWriter(Protocol):
    @abstractmethod
    async def save_currency(self, currency: Currency) -> None:
        raise NotImplementedError

    @abstractmethod
    async def remove_currency(self, currency_id: CurrencyId) -> None:
        raise NotImplementedError
