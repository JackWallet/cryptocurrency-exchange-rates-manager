from dishka import Provider, Scope, provide_all

from application.interactors.currency.add_currency import (
    AddCurrency,
)
from application.interactors.currency.get_currency_by_id import (
    GetCurrencyById,
)
from application.interactors.currency.remove_currency_by_id import (
    RemoveCurrencyById,
)
from application.interactors.price_history.add_price_history import (
    AddPriceHistory,
)
from application.interactors.price_history.get_highest_recorded_price import (
    GetHighestRecordedPrice,
)
from application.interactors.price_history.get_price_history_by_currency_id import (
    GetPriceHistoryByCurrencyId,
)
from application.interactors.price_history.get_price_history_by_id import (
    GetPriceHistoryById,
)
from application.interactors.price_history.remove_price_history_by_id import (
    RemovePriceHistoryById,
)


class PriceHistoryInteractorsProvider(Provider):
    scope = Scope.REQUEST

    interactors = provide_all(
        AddPriceHistory,
        GetHighestRecordedPrice,
        GetPriceHistoryByCurrencyId,
        GetPriceHistoryById,
        RemovePriceHistoryById,
    )


class CurrencyInteractorsProvider(Provider):
    scope = Scope.REQUEST

    interactors = provide_all(
        AddCurrency,
        GetCurrencyById,
        RemoveCurrencyById,
    )
