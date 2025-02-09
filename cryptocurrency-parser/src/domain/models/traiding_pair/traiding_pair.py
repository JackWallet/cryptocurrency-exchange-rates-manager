from dataclasses import dataclass
from datetime import datetime
from domain.models.traiding_pair.traiding_pair_id import TraidingPairId
from domain.models.currency.currency_id import CurrencyId


@dataclass
class TraidingPair:
    id: TraidingPairId
    base_currency_id: CurrencyId
    quote_currency_id: CurrencyId
    created_at: datetime
