from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId
from cryptocurrency_parser.domain.models.price_history.price_history_id import (
    PriceHistoryId,
)


@dataclass
class PriceHistory:
    id: PriceHistoryId | None
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
    percent_change_7d: float
    percent_change_30d: float
    percent_change_60d: float
    percent_change_90d: float
