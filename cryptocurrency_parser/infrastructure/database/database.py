from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from cryptocurrency_parser.application.common.database import Database
from cryptocurrency_parser.entrypoints.config import PostgresConfig


class SQLAlchemyDatabase(Database[AsyncSession]):
    def __init__(self, config: PostgresConfig) -> None:
        self._engine: AsyncEngine = create_async_engine(url=config.url)
        self._session_factory = async_sessionmaker(
            self._engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._session_factory() as session, session.begin():
            yield session

    async def dispose(self) -> None:
        await self._engine.dispose()
