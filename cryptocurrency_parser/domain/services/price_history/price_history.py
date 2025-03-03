from datetime import datetime
from decimal import Decimal
from typing import Optional

from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId
from domain.models.price_history.price_history import PriceHistory


class PriceHistoryService:
    def create_price_history(
        self,
        currency_id: CurrencyId,
        market_cap: Decimal,
        market_cap_dominance: float,
        price: Decimal,
        volume_24h: Decimal,
        max_supply: Optional[int],
        circulating_supply: int,
        percent_change_1h: float,
        percent_change_24h: float,
        percent_change_7d: float,
        percent_change_30d: float,
        percent_change_60d: float,
        percent_change_90d: float,
    ) -> PriceHistory:
        return PriceHistory(
            id=None,
            currency_id=currency_id,
            market_cap=market_cap,
            market_cap_dominance=market_cap_dominance,
            price=price,
            volume_24h=volume_24h,
            max_supply=max_supply,
            circulating_supply=circulating_supply,
            percent_change_1h=percent_change_1h,
            percent_change_24h=percent_change_24h,
            percent_change_30d=percent_change_30d,
            percent_change_60d=percent_change_60d,
            percent_change_7d=percent_change_7d,
            percent_change_90d=percent_change_90d,
            updated_at=datetime.now(),
        )
