from abc import abstractmethod
from contextlib import AbstractAsyncContextManager
from typing import Protocol


class TransactionManager(Protocol):
    @abstractmethod
    def transaction(self) -> AbstractAsyncContextManager:
        pass
