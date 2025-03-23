from dishka import Provider, provide

from cryptocurrency_parser.application.common.transaction_manager import (
    TransactionManager,
)
from cryptocurrency_parser.infrastructure.database.transaction_manager import (
    SQLAlchemyTransactionManager,
)


class SQLAlchemyTransactionManagerProvider(Provider):
    transaction_manager = provide(
        SQLAlchemyTransactionManager, provides=TransactionManager,
    )
