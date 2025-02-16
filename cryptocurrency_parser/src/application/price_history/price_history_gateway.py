from abc import abstractmethod
from typing import Protocol

from cryptocurrency_parser.src.domain.models.currency.currency_id import CurrencyId
from cryptocurrency_parser.src.domain.models.price_history.price_history import (
    PriceHistory,
)


class PriceHistoryReader(Protocol):
    @abstractmethod
    async def get_by_currency_id(
        self, currency_ids: list[CurrencyId]
    ) -> list[PriceHistory]:
        raise NotImplementedError

    @abstractmethod
    async def get_the_highest_recorded_price(
        self, currency_full_name: list[str]
    ) -> list[PriceHistory]:
        raise NotImplementedError

    @abstractmethod
    async def get_last_record(
        self, currency_full_names: list[str]
    ) -> list[PriceHistory]:
        raise NotImplementedError


class PriceHistoryWriter(Protocol):
    @abstractmethod
    async def add_price_history_record(self, price_history: PriceHistory) -> None:
        raise NotImplementedError
