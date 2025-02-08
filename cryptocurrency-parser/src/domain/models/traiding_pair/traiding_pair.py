from dataclasses import dataclass
from datetime import datetime
from domain.models.traiding_pair.traiding_pair_id import TraidingPairId

@dataclass
class TraidingPair:
    id: TraidingPairId
    base_currency_id: int
    quote_currency_id: int
    created_at: datetime