from unittest.mock import AsyncMock

import pytest

from application.interactors.exceptions import PriceHistoryRecordNotFoundError
from application.interactors.price_history.get_highest_recorded_price import (
    GetHighestRecordedPrice,
    GetHighestRecordedPriceDTO,
)
from domain.models.price_history.price_history import PriceHistory


@pytest.mark.asyncio
async def test_get_highest_recorded_price_exists(
    reader_found: AsyncMock,
    mock_price_history: PriceHistory,
) -> None:
    usecase: GetHighestRecordedPrice = GetHighestRecordedPrice(
        price_history_reader=reader_found,
    )
    input_dto: GetHighestRecordedPriceDTO = GetHighestRecordedPriceDTO(
        currency_id=mock_price_history.currency_id,
    )
    result = await usecase(data=input_dto)
    assert result.price_history == mock_price_history


@pytest.mark.asyncio
async def test_get_highest_recorded_price_does_not_exist(
    reader_not_found: AsyncMock,
    mock_price_history: PriceHistory,
) -> None:
    usecase: GetHighestRecordedPrice = GetHighestRecordedPrice(
        price_history_reader=reader_not_found,
    )
    input_dto: GetHighestRecordedPriceDTO = GetHighestRecordedPriceDTO(
        currency_id=mock_price_history.currency_id,
    )
    with pytest.raises(PriceHistoryRecordNotFoundError) as err:
        await usecase(data=input_dto)

    assert err.value._entity_id == str(mock_price_history.currency_id)  # noqa: SLF001
