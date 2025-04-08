from dishka.integrations.fastapi import (
    setup_dishka,
)

from entrypoints.ioc.registry import get_providers
from entrypoints.ioc.setup import create_async_container
from entrypoints.setup import (
    get_fastapi_app,
)

fastapi_app = get_fastapi_app()
provider_registry = get_providers()
dishka_container = create_async_container(providers=provider_registry)

setup_dishka(container=dishka_container, app=fastapi_app)
