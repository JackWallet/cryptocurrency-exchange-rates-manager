from collections.abc import AsyncGenerator

from dishka import Provider, Scope, from_context, provide
from sqlalchemy.ext.asyncio import AsyncSessionTransaction

from cryptocurrency_parser.entrypoints.config import Config
from cryptocurrency_parser.infrastructure.database.database import (
    SQLAlchemyDatabase,
)
from cryptocurrency_parser.infrastructure.database.transaction_manager import (
    SQLAlchemyTransactionManager,
)


class SQLAlchemyProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def provide_database_engine(
        self,
        config: Config,
    ) -> SQLAlchemyDatabase:
        return SQLAlchemyDatabase(config.postgres_config)

    @provide(scope=Scope.REQUEST)
    async def provide_transaction_manager(
        self,
        database: SQLAlchemyDatabase,
    ) -> AsyncGenerator[AsyncSessionTransaction, None]:
        async with database.get_session() as session:
            transaction_manager = SQLAlchemyTransactionManager(session=session)
            async with transaction_manager.transaction() as transaction:
                yield transaction
