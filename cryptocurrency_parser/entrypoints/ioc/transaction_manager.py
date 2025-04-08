from dishka import Provider, Scope, provide

from application.common.transaction_manager import (
    TransactionManager,
)
from infrastructure.database.transaction_manager import (
    SQLAlchemyTransactionManager,
)


class SQLAlchemyTransactionManagerProvider(Provider):
    scope = Scope.REQUEST

    transaction_manager = provide(
        SQLAlchemyTransactionManager,
        provides=TransactionManager,
    )
