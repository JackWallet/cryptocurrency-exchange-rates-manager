from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from cryptocurrency_parser.application.common.transaction_manager import (
    TransactionManager,
)


class SQLAlchemyTransactionManager(TransactionManager):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        try:
            await self._session.commit()
        except SQLAlchemyError:
            await self.rollback()
            raise

    async def rollback(self) -> None:
        await self._session.rollback()
