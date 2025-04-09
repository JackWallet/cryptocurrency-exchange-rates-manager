from datetime import UTC, datetime
from decimal import Decimal
from unittest.mock import AsyncMock

import pytest
import pytest_asyncio

from domain.models.currency.currency import Currency
from domain.models.currency.currency_id import CurrencyId
from domain.models.price_history.price_history import (
    PriceHistory,
)
from domain.models.price_history.price_history_id import (
    PriceHistoryId,
)


@pytest.fixture
def mock_currency() -> Currency:
    return Currency(
        id=CurrencyId(1221),
        ticker="BTC",
        full_name="bitcoin",
        circulating_supply=121,
        last_updated=datetime.now(tz=UTC),
        max_supply=12,
    )


@pytest.fixture
def mock_price_history() -> PriceHistory:
    return PriceHistory(
        id=PriceHistoryId(123),
        currency_id=CurrencyId(1),
        updated_at=datetime.now(tz=UTC),
        circulating_supply=1,
        market_cap=Decimal(1),
        market_cap_dominance=1,
        price=Decimal(1),
        percent_change_1h=1.0,
        percent_change_24h=1.0,
        percent_change_30d=1.0,
        percent_change_60d=1.0,
        percent_change_7d=1.0,
        percent_change_90d=1.0,
        volume_24h=Decimal(1),
    )


@pytest_asyncio.fixture
async def reader_not_found() -> AsyncMock:
    reader = AsyncMock()
    reader.get_currency_by_id = AsyncMock(return_value=None)
    reader.get_currency_by_ticker = AsyncMock(return_value=None)
    reader.get_highest_recorded_price_by_currency_id = AsyncMock(
        return_value=None,
    )
    reader.get_price_history_by_id = AsyncMock(return_value=None)
    reader.get_price_history_by_currency_id = AsyncMock(return_value=None)
    reader.get_price_history_by_currency_ids = AsyncMock(return_value=None)
    reader.get_last_record_by_currency_id = AsyncMock(return_value=None)

    return reader


@pytest_asyncio.fixture
async def reader_found(
    mock_currency: Currency,
    mock_price_history: PriceHistory,
) -> AsyncMock:
    reader = AsyncMock()
    reader.get_currency_by_id = AsyncMock(return_value=mock_currency)
    reader.get_currency_by_ticker = AsyncMock(return_value=mock_currency)
    reader.get_highest_recorded_price_by_currency_id = AsyncMock(
        return_value=mock_price_history,
    )
    reader.get_price_history_by_id = AsyncMock(return_value=mock_price_history)
    reader.get_price_history_by_currency_id = AsyncMock(
        return_value=mock_price_history,
    )
    reader.get_price_history_by_currency_ids = AsyncMock(
        return_value=mock_price_history,
    )
    reader.get_last_record_by_currency_id = AsyncMock(
        return_value=mock_price_history,
    )

    return reader


@pytest_asyncio.fixture
async def adder() -> AsyncMock:
    adder = AsyncMock()
    adder.save_currency = AsyncMock(return_value=None)
    adder.add_price_history_record = AsyncMock(return_value=None)
    return adder


@pytest_asyncio.fixture
async def remover() -> AsyncMock:
    remover = AsyncMock()
    remover.remove_currency_by_id = AsyncMock(return_value=None)
    remover.remove_currency_by_ticker = AsyncMock(return_value=None)
    remover.remove_price_history_record_by_id = AsyncMock(return_value=None)
    return remover


@pytest_asyncio.fixture
async def transaction_manager() -> AsyncMock:
    transaction_manager = AsyncMock()
    transaction_manager.commit = AsyncMock()
    transaction_manager.rollback = AsyncMock()

    return transaction_manager
