import pytest
from sqlalchemy import select
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.asyncio import AsyncSession

from cryptocurrency_parser.entrypoints.config import (
    PostgresConfig,
)
from cryptocurrency_parser.infrastructure.database.database import (
    SQLAlchemyDatabase,
)


@pytest.fixture(scope="package")
def database() -> SQLAlchemyDatabase:
    config: PostgresConfig = PostgresConfig.from_env()
    return SQLAlchemyDatabase(config=config)


@pytest.mark.asyncio
async def test_can_establish_database_connection(
    database: SQLAlchemyDatabase,
) -> None:
    async with database.get_session() as session:
        assert isinstance(session, AsyncSession)


@pytest.mark.asyncio
async def test_can_close_the_db_connection(
    database: SQLAlchemyDatabase,
) -> None:
    await database.dispose()

    with pytest.raises(InvalidRequestError):
        async with database.get_session() as session, session.begin():
            await session.execute(select())
