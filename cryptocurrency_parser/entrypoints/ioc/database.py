from collections.abc import AsyncIterable

from dishka import Provider, Scope, from_context, provide
from sqlalchemy.ext.asyncio import AsyncSession

from application.common.database import Database
from entrypoints.config import Config
from infrastructure.database.database import (
    SQLAlchemyDatabase,
)


class SQLAlchemyDatabaseProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def provide_database_engine(
        self,
        config: Config,
    ) -> Database[AsyncSession]:
        return SQLAlchemyDatabase(config.postgres_config)

    @provide(scope=Scope.REQUEST)
    async def provide_session(
        self,
        database: Database[AsyncSession],
    ) -> AsyncIterable[AsyncSession]:
        async with database.get_session() as session:
            yield session
