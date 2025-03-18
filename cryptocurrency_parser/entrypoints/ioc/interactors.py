from dishka import Provider, Scope, provide_all

from cryptocurrency_parser.application.interactors.currency.add_currency import (
    AddCurrency,
)
from cryptocurrency_parser.application.interactors.currency.get_currency import (
    GetCurrency,
)
from cryptocurrency_parser.application.interactors.currency.remove_currency import (
    RemoveCurrency,
)
from cryptocurrency_parser.application.interactors.price_history.add_price_history import (
    AddPriceHistory,
)
from cryptocurrency_parser.application.interactors.price_history.get_highest_recorded_price import (
    GetHighestRecordedPrice,
)
from cryptocurrency_parser.application.interactors.price_history.get_price_history_by_currency_id import (
    GetPriceHistoryByCurrencyId,
)
from cryptocurrency_parser.application.interactors.price_history.get_price_history_by_id import (
    GetPriceHistoryById,
)
from cryptocurrency_parser.application.interactors.price_history.remove_price_history_by_id import (
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
        GetCurrency,
        RemoveCurrency,
    )
