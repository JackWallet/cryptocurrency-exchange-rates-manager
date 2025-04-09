from typing import Any
from unittest.mock import AsyncMock

import pytest

from application.interactors.price_history.add_price_history import (
    AddPriceHistory,
    AddPriceHistoryDTO,
)
from domain.models.currency.currency import Currency


@pytest.mark.asyncio
async def test_add_price_history(
    adder: AsyncMock,
    mock_price_history: Currency,
    transaction_manager: AsyncMock,
) -> None:
    usecase: AddPriceHistory = AddPriceHistory(
        price_history_adder=adder,
        transaction_manager=transaction_manager,
    )
    price_history_input: dict[str, Any] = mock_price_history.__dict__
    del price_history_input["id"]

    input_dto: AddPriceHistoryDTO = AddPriceHistoryDTO(
        **price_history_input,
    )

    await usecase(data=input_dto)
