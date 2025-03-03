from dataclasses import dataclass

from domain.models.price_history.price_history import PriceHistory
from domain.models.price_history.price_history_id import PriceHistoryId
from application.common.interactor import Interactor
from application.price_history.price_history_gateway import PriceHistoryReader


@dataclass(frozen=True)
class GetPriceHistoryDTO:
    price_history_id: PriceHistoryId


class GetPriceHistoryById(Interactor[GetPriceHistoryDTO, PriceHistory]):
    def __init__(
        self,
        price_history_db_gateway: PriceHistoryReader,
    ) -> None:
        self._price_history_db_gateway = price_history_db_gateway

    async def __call__(self, data: GetPriceHistoryDTO) -> PriceHistory:
        return await self._price_history_db_gateway.get_by_id(
            price_history_id=data.price_history_id
        )
