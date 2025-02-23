from abc import abstractmethod
from typing import Protocol

from cryptocurrency_parser.src.domain.models.currency.currency_id import CurrencyId
from cryptocurrency_parser.src.domain.models.price_history.price_history import (
    PriceHistory,
)
from cryptocurrency_parser.src.domain.models.price_history.price_history_id import (
    PriceHistoryId,
)


class PriceHistoryReader(Protocol):
    @abstractmethod
    async def get_by_id(self, price_history_id: PriceHistoryId) -> PriceHistory:
        raise NotImplementedError

    @abstractmethod
    async def get_by_currency_id(self, currency_id: CurrencyId) -> PriceHistory:
        raise NotImplementedError

    @abstractmethod
    async def get_by_currency_ids(
        self, currency_ids: list[CurrencyId]
    ) -> list[PriceHistory]:
        raise NotImplementedError

    @abstractmethod
    async def get_highest_recorded_price(
        self, currency_full_name: str
    ) -> PriceHistory:
        raise NotImplementedError

    @abstractmethod
    async def get_last_record(
        self, currency_full_names: list[str]
    ) -> list[PriceHistory]:
        raise NotImplementedError


class PriceHistoryAdder(Protocol):
    @abstractmethod
    async def add_price_history_record(self, price_history: PriceHistory) -> None:
        raise NotImplementedError


class PriceHistoryRemover(Protocol):
    @abstractmethod
    async def remove_price_history_record_by_id(
        self, price_history_id: PriceHistoryId
    ) -> None:
        raise NotImplementedError
