from unittest.mock import AsyncMock

import pytest

from application.currency.exceptions import (
    CurrencyTickerAlreadyInDatabaseError,
)
from application.interactors.currency.add_currency import (
    AddCurrency,
    AddCurrencyDTO,
)
from domain.models.currency.currency import Currency


@pytest.mark.asyncio
async def test_add_currency(
    reader_not_found: AsyncMock,
    adder: AsyncMock,
    mock_currency: Currency,
    transaction_manager: AsyncMock,
) -> None:
    usecase: AddCurrency = AddCurrency(
        currency_adder=adder,
        currency_reader=reader_not_found,
        transaction_manager=transaction_manager,
    )
    input_dto: AddCurrencyDTO = AddCurrencyDTO(
        ticker=mock_currency.ticker,
        max_supply=mock_currency.max_supply,
        circulating_supply=mock_currency.circulating_supply,
        full_name=mock_currency.full_name,
    )

    await usecase(data=input_dto)


@pytest.mark.asyncio
async def test_add_currency_already_exists(
    reader_found: AsyncMock,
    adder: AsyncMock,
    mock_currency: Currency,
    transaction_manager: AsyncMock,
) -> None:
    usecase: AddCurrency = AddCurrency(
        currency_adder=adder,
        currency_reader=reader_found,
        transaction_manager=transaction_manager,
    )
    input_dto: AddCurrencyDTO = AddCurrencyDTO(
        ticker=mock_currency.ticker,
        max_supply=mock_currency.max_supply,
        circulating_supply=mock_currency.circulating_supply,
        full_name=mock_currency.full_name,
    )
    with pytest.raises(CurrencyTickerAlreadyInDatabaseError) as ex:
        await usecase(data=input_dto)

    assert ex.value._ticker == mock_currency.ticker  # noqa: SLF001
