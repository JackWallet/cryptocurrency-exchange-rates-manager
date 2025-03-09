from abc import abstractmethod
from contextlib import AbstractAsyncContextManager
from typing import Protocol, TypeVar

SessionType = TypeVar("SessionType")


class TransactionManager(Protocol):
    @abstractmethod
    async def transaction(self) -> AbstractAsyncContextManager[SessionType]:
        pass
