from collections.abc import AsyncGenerator

from dishka import Provider, Scope, from_context, provide
from sqlalchemy.ext.asyncio import AsyncSession

from cryptocurrency_parser.entrypoints.config import Config
from cryptocurrency_parser.infrastructure.database.database import (
    SQLAlchemyDatabase,
)


class SQLAlchemyDatabaseProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def provide_database_engine(
        self,
        config: Config,
    ) -> SQLAlchemyDatabase:
        return SQLAlchemyDatabase(config.postgres_config)

    @provide(scope=Scope.REQUEST)
    async def provide_session(
        self,
        database: SQLAlchemyDatabase,
    ) -> AsyncGenerator[AsyncSession, None]:
        async with database.get_session() as session:
            yield session
