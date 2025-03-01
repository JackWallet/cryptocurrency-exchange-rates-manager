from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from application.common.database import Database
from infrastructure.database.config import DatabaseConfig


class SQLAlchemyDatabase(Database[AsyncSession]):
    def __init__(self, config: DatabaseConfig) -> None:
        self._engine: AsyncEngine = create_async_engine(url=config.url)
        self._session_factory = async_sessionmaker(
            self._engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
        )
<<<<<<< HEAD

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:  # type: ignore
=======
    # For some reason both pylance and MyPy keep giving me a typing error
    # despite the fact that this method has actually the correct
    # syntax. I add ignors because I've got not a single idea on
    # how I can make type checkers recognize this thing
    @asynccontextmanager 
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]: # type: ignore
>>>>>>> 8ca4cdcd9531eb4d968a83fde5d40b84f2e087a5
        async with self._session_factory() as session, session.begin():
            yield session

    async def dispose(self) -> None:
<<<<<<< HEAD
        await self._engine.dispose()
=======
        await self._engine.dispose()
>>>>>>> 8ca4cdcd9531eb4d968a83fde5d40b84f2e087a5
