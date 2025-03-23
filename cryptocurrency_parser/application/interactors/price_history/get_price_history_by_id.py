from dataclasses import dataclass

from cryptocurrency_parser.application.common.interactor import Interactor
from cryptocurrency_parser.application.interactors.exceptions import (
    PriceHistoryRecordNotFoundError,
)
from cryptocurrency_parser.application.price_history.price_history_gateway import (
    PriceHistoryReader,
)
from cryptocurrency_parser.domain.models.price_history.price_history import (
    PriceHistory,
)
from cryptocurrency_parser.domain.models.price_history.price_history_id import (
    PriceHistoryId,
)


@dataclass(frozen=True)
class GetPriceHistoryDTO:
    price_history_id: PriceHistoryId


@dataclass(frozen=True)
class PriceHistoryResultDTO:
    price_history: PriceHistory


class GetPriceHistoryById(
    Interactor[GetPriceHistoryDTO, PriceHistoryResultDTO],
):
    def __init__(
        self,
        price_history_db_gateway: PriceHistoryReader,
    ) -> None:
        self._price_history_db_gateway = price_history_db_gateway

    async def __call__(
        self,
        data: GetPriceHistoryDTO,
    ) -> PriceHistoryResultDTO:
        price_history = await self._price_history_db_gateway.get_by_id(
            price_history_id=data.price_history_id,
        )
        if price_history is None:
            raise PriceHistoryRecordNotFoundError(
                entity_id=str(data.price_history_id),
            )

        return PriceHistoryResultDTO(price_history=price_history)
