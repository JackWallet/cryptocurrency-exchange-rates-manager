from typing import Protocol
from domain.models.currency.currency_id import CurrencyId
from domain.models.currency.currency import Currency


class CoinReader(Protocol):
    async def get_currency(self, currency_id: CurrencyId) -> Currency: ...


class CoinSaver(Protocol):
    async def save_currency(self, currency: Currency) -> None: ...


class CoinRemover(Protocol):
    async def remove_currency(self, currency_id: CurrencyId) -> None: ...
