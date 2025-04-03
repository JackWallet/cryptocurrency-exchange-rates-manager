from datetime import UTC, datetime
from decimal import Decimal
from unittest.mock import AsyncMock

import pytest
import pytest_asyncio

from cryptocurrency_parser.domain.models.currency.currency import Currency
from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId
from cryptocurrency_parser.domain.models.price_history.price_history import (
    PriceHistory,
)
from cryptocurrency_parser.domain.models.price_history.price_history_id import (
    PriceHistoryId,
)


@pytest_asyncio.fixture
async def reader() -> AsyncMock:
    return AsyncMock()


@pytest_asyncio.fixture
async def adder() -> AsyncMock:
    return AsyncMock()


@pytest_asyncio.fixture
async def remover() -> AsyncMock:
    return AsyncMock()


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
async def transaction_manager() -> AsyncMock:
    transaction_manager = AsyncMock()
    transaction_manager.commit = AsyncMock()
    transaction_manager.rollback = AsyncMock()

    return transaction_manager
