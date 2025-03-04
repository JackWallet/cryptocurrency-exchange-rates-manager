from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId


@dataclass
class Currency:
    id: Optional[CurrencyId]
    ticker: str
    full_name: str
    max_supply: Optional[int]
    circulating_supply: int
    last_updated: Optional[datetime]