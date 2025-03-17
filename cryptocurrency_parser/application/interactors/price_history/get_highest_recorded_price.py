from dataclasses import dataclass

from cryptocurrency_parser.application.common.interactor import Interactor
from cryptocurrency_parser.application.interactors.exceptions import (
    PriceHistoryRecordNotFoundError,
)
from cryptocurrency_parser.application.price_history.price_history_gateway import (
    PriceHistoryReader,
)
from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId
from cryptocurrency_parser.domain.models.price_history.price_history import (
    PriceHistory,
)


@dataclass(frozen=True)
class GetHighestRecordedPriceDTO:
    currency_id: CurrencyId


class GetHighestRecordedPrice(
    Interactor[GetHighestRecordedPriceDTO, PriceHistory],
):
    def __init__(
        self,
        price_history_db_gateway: PriceHistoryReader,
    ) -> None:
        self._price_history_db_gateway = price_history_db_gateway

    async def __call__(self, data: GetHighestRecordedPriceDTO) -> PriceHistory:
        price_history = await self._price_history_db_gateway.get_highest_recorded_price_by_currency_id(
            currency_id=data.currency_id,
        )

        if price_history is None:
            raise PriceHistoryRecordNotFoundError(
                entity_id=str(data.currency_id),
            )
        return price_history
