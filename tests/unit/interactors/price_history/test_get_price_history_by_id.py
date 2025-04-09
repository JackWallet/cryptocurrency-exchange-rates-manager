from unittest.mock import AsyncMock

import pytest

from application.interactors.exceptions import PriceHistoryRecordNotFoundError
from application.interactors.price_history.get_price_history_by_id import (
    GetPriceHistoryById,
    GetPriceHistoryByIdDTO,
)
from domain.models.price_history.price_history import PriceHistory


@pytest.mark.asyncio
async def test_get_price_history_by_id_exists(
    reader_found: AsyncMock,
    mock_price_history: PriceHistory,
) -> None:
    usecase: GetPriceHistoryById = GetPriceHistoryById(
        price_history_reader=reader_found,
    )
    input_dto: GetPriceHistoryByIdDTO = GetPriceHistoryByIdDTO(
        price_history_id=mock_price_history.id,  # type: ignore[arg-type]
    )
    result = await usecase(data=input_dto)
    assert result.price_history == mock_price_history


@pytest.mark.asyncio
async def test_get_price_history_by_id_does_not_exist(
    reader_not_found: AsyncMock,
    mock_price_history: PriceHistory,
) -> None:
    usecase: GetPriceHistoryById = GetPriceHistoryById(
        price_history_reader=reader_not_found,
    )
    input_dto: GetPriceHistoryByIdDTO = GetPriceHistoryByIdDTO(
        price_history_id=mock_price_history.id,  # type: ignore[arg-type]
    )
    with pytest.raises(PriceHistoryRecordNotFoundError) as err:
        await usecase(data=input_dto)

    assert err.value._entity_id == str(mock_price_history.id)  # noqa: SLF001
