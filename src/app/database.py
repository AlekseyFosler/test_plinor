from sqlalchemy import ChunkedIteratorResult
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.models.base import Base
from app.settings import settings


class Session:
    def __init__(self):
        self.engine = create_async_engine(
            url=settings.STORAGE_URI,
            echo=False,
            echo_pool=False,
            pool_size=settings.POOL_SIZE,
            max_overflow=settings.MAX_OVERFLOW,
        )
        self.async_session = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )

    async def execute(self, stmt: Base):
        try:
            async with self.async_session() as session:
                async with session.begin():
                    result: ChunkedIteratorResult = await session.execute(stmt)  # noqa
                    return result.scalar_one_or_none()
        except OperationalError as error:
            pass
