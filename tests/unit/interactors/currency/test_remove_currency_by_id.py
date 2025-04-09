from unittest.mock import AsyncMock

import pytest

from application.currency.exceptions import CurrencyNotFoundByIdError
from application.interactors.currency.remove_currency_by_id import (
    RemoveCurrencyById,
    RemoveCurrencyByIdDTO,
)
from domain.models.currency.currency import Currency


@pytest.mark.asyncio
async def test_remove_currency_by_id_exists(
    reader_found: AsyncMock,
    remover: AsyncMock,
    mock_currency: Currency,
    transaction_manager: AsyncMock,
) -> None:
    usecase: RemoveCurrencyById = RemoveCurrencyById(
        currency_reader=reader_found,
        currency_remover=remover,
        transaction_manager=transaction_manager,
    )
    input_dto: RemoveCurrencyByIdDTO = RemoveCurrencyByIdDTO(
        currency_id=mock_currency.id, # type: ignore[arg-type]
    )
    await usecase(data=input_dto)

@pytest.mark.asyncio
async def test_remove_currency_by_id_does_not_exist(
    reader_not_found: AsyncMock,
    remover: AsyncMock,
    mock_currency: Currency,
    transaction_manager: AsyncMock,
) -> None:
    usecase: RemoveCurrencyById = RemoveCurrencyById(
        currency_reader=reader_not_found,
        currency_remover=remover,
        transaction_manager=transaction_manager,
    )
    input_dto: RemoveCurrencyByIdDTO = RemoveCurrencyByIdDTO(
        currency_id=mock_currency.id, # type: ignore[arg-type]
    )
    with pytest.raises(CurrencyNotFoundByIdError):
        await usecase(data=input_dto)
