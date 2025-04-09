from dataclasses import dataclass

from application.common.interactor import Interactor
from application.interactors.exceptions import (
    CurrencyNotFoundError,
)
from application.price_history.price_history_gateway import (
    PriceHistoryReader,
)
from domain.models.currency.currency_id import CurrencyId
from domain.models.price_history.price_history import (
    PriceHistory,
)


@dataclass(frozen=True)
class GetPriceHistoryByCurrencyIdDTO:
    currency_id: CurrencyId


@dataclass(frozen=True)
class GetPriceHistoryByCurrencyIdResultDTO:
    currencies: list[PriceHistory]


class GetPriceHistoryByCurrencyId(
    Interactor[
        GetPriceHistoryByCurrencyIdDTO,
        GetPriceHistoryByCurrencyIdResultDTO,
    ],
):
    def __init__(self, price_history_db_gateway: PriceHistoryReader) -> None:
        self._price_history_db_gateway = price_history_db_gateway

    async def __call__(
        self,
        data: GetPriceHistoryByCurrencyIdDTO,
    ) -> GetPriceHistoryByCurrencyIdResultDTO:
        price_history = await self._price_history_db_gateway.get_price_history_by_currency_id(
            currency_id=data.currency_id,
        )
        if price_history is None:
            raise CurrencyNotFoundError(entity_id=str(data.currency_id))

        return GetPriceHistoryByCurrencyIdResultDTO(currencies=price_history)
