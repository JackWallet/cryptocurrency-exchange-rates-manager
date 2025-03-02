import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import InvalidRequestError

from cryptocurrency_parser.src.entrypoints.config import (
    DatabaseConfig,
    get_postgres_config,
)
from cryptocurrency_parser.src.infrastructure.database.database import (
    SQLAlchemyDatabase,
)


@pytest.fixture(scope="package")
def database() -> SQLAlchemyDatabase:
    config: DatabaseConfig = get_postgres_config()
    return SQLAlchemyDatabase(config=config)

@pytest.mark.asyncio
async def test_can_establish_database_connection(database: SQLAlchemyDatabase) -> None:
    async with database.get_session() as session:
        assert isinstance(session, AsyncSession)

@pytest.mark.asyncio
async def test_can_close_the_db_connection(database: SQLAlchemyDatabase) -> None:
    await database.dispose()

    with pytest.raises(InvalidRequestError):
        async with database.get_session() as session, session.begin():
            await session.execute(select())