from dataclasses import dataclass
from datetime import UTC, datetime

from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId


@dataclass
class Currency:
    id: CurrencyId | None
    ticker: str
    full_name: str
    max_supply: int | None
    circulating_supply: int
    last_updated: datetime | None

    @classmethod
    def create(
        cls,
        ticker: str,
        full_name: str,
        max_supply: int | None,
        circulating_supply: int,
    ) -> "Currency":
        return cls(
            id=None,
            ticker=ticker,
            full_name=full_name,
            max_supply=max_supply,
            circulating_supply=circulating_supply,
            last_updated=datetime.now(tz=UTC),
        )
