from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


CONNECTION_TIMEOUT = 60
CACHE_SIZE = 0


class DataBase:
    url: str
    async_session: AsyncSession
    engine: AsyncEngine

    def __init__(self, url):
        self.url = url
        if self.url:
            self.engine = create_async_engine(
                self.url,
                poolclass=NullPool,
                connect_args={
                    "timeout": CONNECTION_TIMEOUT,
                    "statement_cache_size": CACHE_SIZE
                }
            )
            self.async_session = sessionmaker(
                self.engine,
                expire_on_commit=False,
                class_=AsyncSession
            )
        else:
            raise Exception("Database URL not provided")
