from dataclasses import dataclass

from domain.models.price_history.price_history_id import (
    PriceHistoryId,
)

from application.common.interactor import Interactor
from application.interactors.exceptions import (
    PriceHistoryRecordNotFoundError,
)
from application.price_history.price_history_gateway import (
    PriceHistoryReader,
    PriceHistoryRemover,
)


@dataclass(frozen=True)
class RemovePriceHistoryByIdDTO:
    price_history_id: PriceHistoryId


class RemovePriceHistoryById(Interactor[RemovePriceHistoryByIdDTO, None]):
    def __init__(
        self,
        price_history_reader: PriceHistoryReader,
        price_history_remover: PriceHistoryRemover,
    ) -> None:
        self._price_history_remover = price_history_remover
        self._price_history_reader = price_history_reader

    async def __call__(self, data: RemovePriceHistoryByIdDTO) -> None:
        if not await self._price_history_reader.get_by_id(
            data.price_history_id,
        ):
            raise PriceHistoryRecordNotFoundError(
                entity_id=str(data.price_history_id),
            )
        await self._price_history_remover.remove_price_history_record_by_id(
            price_history_id=data.price_history_id,
        )
