from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager
from typing import Generic, TypeVar

SessionType = TypeVar("SessionType")


class Database(ABC, Generic[SessionType]):
    @abstractmethod
    def get_session(self) -> AbstractAsyncContextManager[SessionType]:
        pass

    @abstractmethod
    async def dispose(self) -> None:
        pass
