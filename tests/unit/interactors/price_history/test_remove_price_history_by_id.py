from unittest.mock import AsyncMock

import pytest

from application.interactors.exceptions import PriceHistoryRecordNotFoundError
from application.interactors.price_history.remove_price_history_by_id import (
    RemovePriceHistoryById,
    RemovePriceHistoryByIdDTO,
)
from domain.models.price_history.price_history import PriceHistory


@pytest.mark.asyncio
async def test_remove_price_history_by_id_exists(
    reader_found: AsyncMock,
    remover: AsyncMock,
    mock_price_history: PriceHistory,
) -> None:
    usecase: RemovePriceHistoryById = RemovePriceHistoryById(
        price_history_reader=reader_found,
        price_history_remover=remover,
    )
    input_dto = RemovePriceHistoryByIdDTO(
        price_history_id=mock_price_history.id,  # type: ignore[arg-type]
    )
    await usecase(data=input_dto)


@pytest.mark.asyncio
async def test_remove_price_history_by_id_does_not_exist(
    reader_not_found: AsyncMock,
    remover: AsyncMock,
    mock_price_history: PriceHistory,
) -> None:
    usecase: RemovePriceHistoryById = RemovePriceHistoryById(
        price_history_reader=reader_not_found,
        price_history_remover=remover,
    )
    input_dto = RemovePriceHistoryByIdDTO(
        price_history_id=mock_price_history.id,  # type: ignore[arg-type]
    )

    with pytest.raises(PriceHistoryRecordNotFoundError) as err:
        await usecase(data=input_dto)

    assert err.value._entity_id == str(mock_price_history.id)  # noqa: SLF001
