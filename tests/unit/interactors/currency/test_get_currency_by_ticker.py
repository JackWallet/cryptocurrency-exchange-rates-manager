from unittest.mock import AsyncMock

import pytest

from application.currency.exceptions import (
    CurrencyNotFoundByTickerError,
)
from application.interactors.currency.get_currency_by_ticker import (
    GetCurrencyByTicker,
    GetCurrencyByTickerDTO,
    GetCurrencyByTickerResultDTO,
)
from domain.models.currency.currency import Currency


@pytest.mark.asyncio
async def test_get_currency_by_ticker_exists(
    reader_found: AsyncMock,
    mock_currency: Currency,
) -> None:
    usecase: GetCurrencyByTicker = GetCurrencyByTicker(
        currency_reader=reader_found,
    )
    input_dto: GetCurrencyByTickerDTO = GetCurrencyByTickerDTO(
        currency_ticker=mock_currency.ticker,
    )
    result: GetCurrencyByTickerResultDTO = await usecase(
        data=input_dto,
    )
    assert result.currency == mock_currency


@pytest.mark.asyncio
async def test_get_currency_by_id_does_not_exist(
    reader_not_found: AsyncMock,
    mock_currency: Currency,
) -> None:
    usecase: GetCurrencyByTicker = GetCurrencyByTicker(
        currency_reader=reader_not_found,
    )
    input_dto: GetCurrencyByTickerDTO = GetCurrencyByTickerDTO(
        currency_ticker=mock_currency.ticker,
    )
    with pytest.raises(CurrencyNotFoundByTickerError) as ex:
        await usecase(data=input_dto)

    assert ex.value._identifier == str(mock_currency.ticker)  # noqa: SLF001
