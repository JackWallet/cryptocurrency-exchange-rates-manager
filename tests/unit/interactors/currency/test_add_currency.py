from unittest.mock import AsyncMock

import pytest

from cryptocurrency_parser.application.interactors.currency.add_currency import (
    AddCurrency,
    AddCurrencyDTO,
)
from cryptocurrency_parser.domain.models.currency.currency import Currency


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
