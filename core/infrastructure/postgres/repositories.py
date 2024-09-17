from abc import ABC
from abc import abstractmethod
from decouple import config

from galery_api.infrastructure.postgres.tables import BaseTable

# TODO: fix db connection
from core.infrastructure.postgres.database import DataBase


DATABASE_URL = config("DATABASE_URL", "")


class BaseRepository(ABC):
    table: BaseTable
    db: DataBase

    def __init__(self):
        self.db = DataBase(DATABASE_URL)
    
    async def get_session(self):
        async with self.db.async_session() as session:
            yield session
    
    async def execute_query(self, query):
        async with self.db.async_session() as session:
            async with session.begin():
                result = await session.execute(query)
                return result

    @abstractmethod
    async def create(self):
        raise NotImplementedError()

    @abstractmethod
    async def list(self):
        raise NotImplementedError()

    @abstractmethod
    async def update(self):
        raise NotImplementedError()

    @abstractmethod
    async def delete(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def get(self):
        raise NotImplementedError()
