from unittest.mock import AsyncMock

import pytest

from application.currency.exceptions import CurrencyNotFoundByIdError
from application.interactors.currency.get_currency_by_id import (
    GetCurrencyById,
    GetCurrencyByIdDTO,
    GetCurrencyByIdResultDTO,
)
from domain.models.currency.currency import Currency


@pytest.mark.asyncio
async def test_get_currency_by_id_exists(
    reader_found: AsyncMock,
    mock_currency: Currency,
) -> None:
    usecase: GetCurrencyById = GetCurrencyById(
        currency_reader=reader_found,
    )
    input_dto: GetCurrencyByIdDTO = GetCurrencyByIdDTO(
        currency_id=mock_currency.id, # type: ignore[arg-type]
    )
    result: GetCurrencyByIdResultDTO = await usecase(
        data=input_dto,
    )
    assert result.currency == mock_currency


@pytest.mark.asyncio
async def test_get_currency_by_id_does_not_exist(
    reader_not_found: AsyncMock,
    mock_currency: Currency,
) -> None:
    usecase: GetCurrencyById = GetCurrencyById(
        currency_reader=reader_not_found,
    )
    input_dto: GetCurrencyByIdDTO = GetCurrencyByIdDTO(
        currency_id=mock_currency.id, # type: ignore[arg-type]
    )
    with pytest.raises(CurrencyNotFoundByIdError) as ex:
        await usecase(data=input_dto)

    assert ex.value._identifier == str(mock_currency.id)  # noqa: SLF001
