from collections.abc import Iterable

from dishka import AsyncContainer, Provider, make_async_container

from cryptocurrency_parser.entrypoints.config import Config, load_config


def create_async_container(
    providers: Iterable[Provider],
) -> AsyncContainer:
    config: Config = load_config()
    return make_async_container(*providers, context={Config: config})
