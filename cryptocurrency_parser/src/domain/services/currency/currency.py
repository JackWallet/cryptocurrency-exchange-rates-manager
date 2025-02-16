from datetime import datetime
from domain.models.currency.currency import Currency

class CurrencyService:
    def create_currency(self) -> Currency:
        last_updated = datetime.now()
        return 