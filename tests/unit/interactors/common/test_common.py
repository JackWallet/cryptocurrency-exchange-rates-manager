from collections.abc import AsyncGenerator
from typing import Any
from unittest.mock import Mock

import pytest_asyncio
from dishka import (
    AsyncContainer,
    Provider,
    Scope,
    make_async_container,
    provide,
)

from cryptocurrency_parser.application.price_history.price_history_gateway import (
    PriceHistoryAdder,
    PriceHistoryReader,
    PriceHistoryRemover,
)


class MockGatewayProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def provide_reader(self) -> PriceHistoryReader:
        reader = Mock()
        reader.execute = Mock(return_value=1)
        return reader

    @provide
    def provide_adder(self) -> PriceHistoryAdder:
        writer = Mock()
        writer.execute = Mock(return_value=1)
        return writer

    @provide
    def provide_remover(self) -> PriceHistoryRemover:
        remover = Mock()
        remover.execute = Mock(return_value=1)
        return remover


@pytest_asyncio.fixture(scope="package")
async def container() -> AsyncGenerator[AsyncContainer, None]:
    container = make_async_container(MockGatewayProvider())
    yield container
    await container.close()


@pytest_asyncio.fixture(scope="package")
async def reader(container: AsyncContainer) -> Any:  # noqa: ANN401
    return await container.get(PriceHistoryReader)


@pytest_asyncio.fixture(scope="package")
async def adder(container: AsyncContainer) -> Any:  # noqa: ANN401
    return await container.get(PriceHistoryAdder)


@pytest_asyncio.fixture(scope="package")
async def remover(container: AsyncContainer) -> Any:  # noqa: ANN401
    return await container.get(PriceHistoryRemover)
