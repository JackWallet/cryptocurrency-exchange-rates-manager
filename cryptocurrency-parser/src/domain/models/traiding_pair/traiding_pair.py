from dataclasses import dataclass
from datetime import datetime
from domain.models.traiding_pair.traiding_pair_id import TraidingPairId
from domain.models.coin.coin_id import CoinId

@dataclass
class TraidingPair:
    id: TraidingPairId
    base_currency_id: CoinId
    quote_currency_id: CoinId
    created_at: datetime