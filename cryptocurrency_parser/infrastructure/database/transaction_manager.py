from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from cryptocurrency_parser.application.common.database import Database
from cryptocurrency_parser.application.common.transaction_manager import (
    TransactionManager,
)


class SQLAlchemyTransactionManager(TransactionManager):
    def __init__(self, database: Database[AsyncSession]) -> None:
        self._database = database

    @asynccontextmanager
    async def transaction(self) -> AsyncGenerator[AsyncSession, None]: # type: ignore  # noqa: PGH003
        async with self._database.get_session() as session, session.begin():
            try:
                yield session
                await session.commit()
            except SQLAlchemyError:
                await session.rollback()
                raise
