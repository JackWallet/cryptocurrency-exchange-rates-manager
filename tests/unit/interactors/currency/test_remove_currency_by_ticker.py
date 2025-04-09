from unittest.mock import AsyncMock

import pytest

from application.currency.exceptions import (
    CurrencyNotFoundByTickerError,
)
from application.interactors.currency.remove_currency_by_ticker import (
    RemoveCurrencyByTicker,
    RemoveCurrencyByTickerDTO,
)
from domain.models.currency.currency import Currency


@pytest.mark.asyncio
async def test_remove_currency_by_ticker_exists(
    reader_found: AsyncMock,
    remover: AsyncMock,
    mock_currency: Currency,
    transaction_manager: AsyncMock,
) -> None:
    usecase: RemoveCurrencyByTicker = RemoveCurrencyByTicker(
        currency_reader=reader_found,
        currency_remover=remover,
        transaction_manager=transaction_manager,
    )
    input_dto: RemoveCurrencyByTickerDTO = RemoveCurrencyByTickerDTO(
        currency_ticker=mock_currency.ticker,  # type: ignore[arg-type]
    )
    await usecase(data=input_dto)


@pytest.mark.asyncio
async def test_remove_currency_by_ticker_does_not_exist(
    reader_not_found: AsyncMock,
    remover: AsyncMock,
    mock_currency: Currency,
    transaction_manager: AsyncMock,
) -> None:
    usecase: RemoveCurrencyByTicker = RemoveCurrencyByTicker(
        currency_reader=reader_not_found,
        currency_remover=remover,
        transaction_manager=transaction_manager,
    )
    input_dto: RemoveCurrencyByTickerDTO = RemoveCurrencyByTickerDTO(
        currency_ticker=mock_currency.ticker,  # type: ignore[arg-type]
    )
    with pytest.raises(CurrencyNotFoundByTickerError):
        await usecase(data=input_dto)
