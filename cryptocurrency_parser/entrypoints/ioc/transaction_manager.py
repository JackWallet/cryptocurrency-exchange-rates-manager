from dishka import Provider, Scope, provide

from cryptocurrency_parser.application.common.transaction_manager import (
    TransactionManager,
)
from cryptocurrency_parser.infrastructure.database.transaction_manager import (
    SQLAlchemyTransactionManager,
)


class SQLAlchemyTransactionManagerProvider(Provider):
    scope = Scope.REQUEST

    transaction_manager = provide(
        SQLAlchemyTransactionManager,
        provides=TransactionManager,
    )
