from dishka import Provider, Scope, provide

from cryptocurrency_parser.application.currency.currency_gateway import (
    CurrencyAdder,
    CurrencyReader,
    CurrencyRemover,
)
from cryptocurrency_parser.application.price_history.price_history_gateway import (
    PriceHistoryAdder,
    PriceHistoryReader,
    PriceHistoryRemover,
)
from cryptocurrency_parser.infrastructure.database.currency.currency_gateways import (
    SQLAlchemyCurrencyAdder,
    SQLAlchemyCurrencyReader,
    SQLAlchemyCurrencyRemover,
)
from cryptocurrency_parser.infrastructure.database.price_history.price_history_gateways import (
    SQLAlchemyPriceHistoryAdder,
    SQLAlchemyPriceHistoryReader,
    SQLAlchemyPriceHistoryRemover,
)


class SQLAlchemyCurrencyRepositoryProvider(Provider):
    scope = Scope.REQUEST

    reader = provide(
        SQLAlchemyCurrencyReader,
        provides=CurrencyReader,
    )
    adder = provide(
        SQLAlchemyCurrencyAdder,
        provides=CurrencyAdder,
    )
    remover = provide(
        SQLAlchemyCurrencyRemover,
        provides=CurrencyRemover,
    )


class SQLAlchemyPriceHistoryRepositoryProvider(Provider):
    scope = Scope.REQUEST

    reader = provide(
        SQLAlchemyPriceHistoryReader,
        provides=PriceHistoryReader,
    )
    adder = provide(
        SQLAlchemyPriceHistoryAdder,
        provides=PriceHistoryAdder,
    )
    remover = provide(
        SQLAlchemyPriceHistoryRemover,
        provides=PriceHistoryRemover,
    )
