from unittest.mock import AsyncMock

import pytest

from application.currency.exceptions import CurrencyNotFoundByIdError
from application.interactors.price_history.get_price_history_by_currency_id import (
    GetPriceHistoryByCurrencyId,
    GetPriceHistoryByCurrencyIdDTO,
)
from domain.models.price_history.price_history import PriceHistory


@pytest.mark.asyncio
async def test_test_get_price_history_by_currency_id_exists(
    reader_found: AsyncMock,
    mock_price_history: PriceHistory,
) -> None:
    usecase: GetPriceHistoryByCurrencyId = GetPriceHistoryByCurrencyId(
        price_history_reader=reader_found,
    )
    input_dto: GetPriceHistoryByCurrencyIdDTO = GetPriceHistoryByCurrencyIdDTO(
        currency_id=mock_price_history.currency_id,
    )
    result = await usecase(data=input_dto)
    assert [mock_price_history] == result.currencies


@pytest.mark.asyncio
async def test_test_get_price_history_by_currency_id_does_not_exist(
    reader_not_found: AsyncMock,
    mock_price_history: PriceHistory,
) -> None:
    usecase: GetPriceHistoryByCurrencyId = GetPriceHistoryByCurrencyId(
        price_history_reader=reader_not_found,
    )
    input_dto: GetPriceHistoryByCurrencyIdDTO = GetPriceHistoryByCurrencyIdDTO(
        currency_id=mock_price_history.currency_id,
    )
    with pytest.raises(CurrencyNotFoundByIdError) as err:
        await usecase(data=input_dto)

    assert err.value._identifier == str(mock_price_history.currency_id)  # noqa: SLF001
