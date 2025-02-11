from domain.models.currency.currency_id import CurrencyId


class Currency:
    id: CurrencyId
    ticker: str
    name: str