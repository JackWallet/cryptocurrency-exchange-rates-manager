from abc import abstractmethod
from contextlib import AbstractAsyncContextManager
from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSessionTransaction


class TransactionManager(Protocol):
    @abstractmethod
    def transaction(
        self,
    ) -> AbstractAsyncContextManager[AsyncSessionTransaction]:
        pass
