from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException, status

from cryptocurrency_parser.application.interactors.exceptions import (
    PriceHistoryRecordNotFoundError,
)
from cryptocurrency_parser.application.interactors.price_history.get_price_history_by_currency_id import (
    GetPriceHistoryByCurrencyId,
    GetPriceHistoryByCurrencyIdDTO,
    GetPriceHistoryByCurrencyIdResultDTO,
)
from cryptocurrency_parser.application.interactors.price_history.get_price_history_by_id import (
    GetPriceHistoryById,
    GetPriceHistoryByIdDTO,
    GetPriceHistoryResultByIdDTO,
)
from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId
from cryptocurrency_parser.domain.models.price_history.price_history_id import (
    PriceHistoryId,
)

start_router = APIRouter()


@start_router.get(path="/price_record/{price_record_id}")
@inject
async def get_price_history(
    price_record_id: int,
    interactor: FromDishka[GetPriceHistoryById],
) -> GetPriceHistoryResultByIdDTO:
    try:
        return await interactor(
            data=GetPriceHistoryByIdDTO(
                price_history_id=PriceHistoryId(price_record_id),
            ),
        )
    except PriceHistoryRecordNotFoundError as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ex),
            headers={"X-Error": "Item not found"},
        ) from ex


@start_router.get(path="/price_record/by_currency/{currency_id}")
@inject
async def get_by_currency_id(
    currency_id: int,
    interactor: FromDishka[GetPriceHistoryByCurrencyId],
) -> GetPriceHistoryByCurrencyIdResultDTO:
    try:
        return await interactor(
            data=GetPriceHistoryByCurrencyIdDTO(
                currency_id=CurrencyId(currency_id),
            ),
        )
    except PriceHistoryRecordNotFoundError as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ex),
            headers={"X-Error": "Item not found"},
        ) from ex
