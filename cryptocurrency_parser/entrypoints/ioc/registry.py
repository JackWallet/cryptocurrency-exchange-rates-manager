from collections.abc import Iterable

from dishka import Provider

from entrypoints.ioc.database import (
    SQLAlchemyDatabaseProvider,
)
from entrypoints.ioc.interactors import (
    CurrencyInteractorsProvider,
    PriceHistoryInteractorsProvider,
)
from entrypoints.ioc.repositories import (
    SQLAlchemyCurrencyRepositoryProvider,
    SQLAlchemyPriceHistoryRepositoryProvider,
)
from entrypoints.ioc.transaction_manager import (
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
