from dataclasses import dataclass

from cryptocurrency_parser.application.common.interactor import Interactor
from cryptocurrency_parser.application.interactors.exceptions import (
    CurrencyNotFoundError,
)
from cryptocurrency_parser.application.price_history.price_history_gateway import (
    PriceHistoryReader,
)
from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId
from cryptocurrency_parser.domain.models.price_history.price_history import (
    PriceHistory,
)


@dataclass(frozen=True)
class GetPriceHistoryByCurrencyIdDTO:
    currency_id: CurrencyId


@dataclass(frozen=True)
class PriceHistoryResultDTO:
    currencies: list[PriceHistory]


class GetPriceHistoryByCurrencyId(
    Interactor[GetPriceHistoryByCurrencyIdDTO, PriceHistoryResultDTO],
):
    def __init__(self, price_history_db_gateway: PriceHistoryReader) -> None:
        self._price_history_db_gateway = price_history_db_gateway

    async def __call__(
        self,
        data: GetPriceHistoryByCurrencyIdDTO,
    ) -> PriceHistoryResultDTO:
        price_history = (
            await self._price_history_db_gateway.get_by_currency_id(
                currency_id=data.currency_id,
            )
        )
        if price_history is None:
            raise CurrencyNotFoundError(entity_id=str(data.currency_id))

        return PriceHistoryResultDTO(currencies=price_history)
