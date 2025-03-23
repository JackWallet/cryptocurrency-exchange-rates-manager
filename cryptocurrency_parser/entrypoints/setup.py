from collections.abc import AsyncGenerator, Iterable
from contextlib import asynccontextmanager

from dishka import AsyncContainer, Provider, make_async_container
from fastapi import FastAPI

from cryptocurrency_parser.entrypoints.config import Config, load_config
from cryptocurrency_parser.presentation.handlers import start_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    yield
    await app.state.dishka_container.close()


def get_fastapi_app() -> FastAPI:
    fastapi_app = FastAPI(lifespan=lifespan)
    fastapi_app.include_router(start_router)

    return fastapi_app


def create_async_container(
    providers: Iterable[Provider],
) -> AsyncContainer:
    config: Config = load_config()
    return make_async_container(*providers, context={Config: config})
