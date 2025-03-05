from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from cryptocurrency_parser.application.common.interactor import Interactor
from cryptocurrency_parser.application.common.transaction_manager import (
    TransactionManager,
)
from cryptocurrency_parser.application.price_history.price_history_gateway import (
    PriceHistoryAdder,
)
from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId
from cryptocurrency_parser.domain.services.price_history.price_history import (
    PriceHistoryService,
)


@dataclass(frozen=True)
class AddPriceHistoryDTO:
    currency_id: CurrencyId
    updated_at: datetime
    market_cap: Decimal
    market_cap_dominance: float
    price: Decimal
    volume_24h: Decimal
    max_supply: int | None
    circulating_supply: int
    percent_change_1h: float
    percent_change_24h: float
    percent_change_30d: float
    percent_change_60d: float
    percent_change_7d: float
    percent_change_90d: float


class AddPriceHistory(Interactor[AddPriceHistoryDTO, None]):
    def __init__(
        self,
        price_history_db_gateway: PriceHistoryAdder,
        price_history_service: PriceHistoryService,
        transaction_manager: TransactionManager,
    ) -> None:
        self._price_history_db_gateway = price_history_db_gateway
        self._price_history_service = price_history_service
        self._transaction_manager = transaction_manager

    async def __call__(self, data: AddPriceHistoryDTO) -> None:
        price_history = self._price_history_service.create_price_history(
            currency_id=data.currency_id,
            market_cap=data.market_cap,
            market_cap_dominance=data.market_cap_dominance,
            price=data.price,
            volume_24h=data.volume_24h,
            max_supply=data.max_supply,
            circulating_supply=data.circulating_supply,
            percent_change_1h=data.percent_change_1h,
            percent_change_24h=data.percent_change_24h,
            percent_change_30d=data.percent_change_30d,
            percent_change_60d=data.percent_change_60d,
            percent_change_7d=data.percent_change_7d,
            percent_change_90d=data.percent_change_90d,
        )
        await self._price_history_db_gateway.add_price_history_record(
            price_history=price_history,
        )
        await self._transaction_manager.commit()
