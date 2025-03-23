from collections.abc import Iterable

from dishka import Provider

from cryptocurrency_parser.entrypoints.ioc.database import (
    SQLAlchemyDatabaseProvider,
)
from cryptocurrency_parser.entrypoints.ioc.interactors import (
    CurrencyInteractorsProvider,
    PriceHistoryInteractorsProvider,
)
from cryptocurrency_parser.entrypoints.ioc.repositories import (
    SQLAlchemyCurrencyRepositoryProvider,
    SQLAlchemyPriceHistoryRepositoryProvider,
)
from cryptocurrency_parser.entrypoints.ioc.transaction_manager import (
    SQLAlchemyTransactionManagerProvider,
)


def get_providers() -> Iterable[Provider]:
    return (
        SQLAlchemyDatabaseProvider(),
        PriceHistoryInteractorsProvider(),
        CurrencyInteractorsProvider(),
        SQLAlchemyCurrencyRepositoryProvider(),
        SQLAlchemyPriceHistoryRepositoryProvider(),
        SQLAlchemyTransactionManagerProvider(),
    )
