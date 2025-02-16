from datetime import datetime
from domain.models.currency.currency_id import CurrencyId


class Currency:
    id: CurrencyId
    ticker: str
    full_name: str
    max_supply: float | None
    circulating_supply: float
    last_updated: datetime