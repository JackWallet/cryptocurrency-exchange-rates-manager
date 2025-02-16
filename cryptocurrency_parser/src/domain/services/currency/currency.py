from datetime import datetime
from domain.models.currency.currency import Currency

class CurrencyService:
    def create_currency(self, full_name: str, ticker: str) -> Currency:
        last_updated = datetime.now()
        return Currency(
            id=None,
            last_updated=last_updated,
            full_name=full_name,
            ticker=ticker
        )