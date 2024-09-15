from abc import ABC
from abc import abstractmethod
from decouple import config
from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from api.tables import BaseTable
from api.tables import ArtworkTable

# TODO: fix db connection
from api.database import DataBase


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
        raise NotImplementedError

    @abstractmethod
    async def list(self):
        raise NotImplementedError

    @abstractmethod
    async def update(self):
        raise NotImplementedError

    @abstractmethod
    async def delete(self):
        raise NotImplementedError
    
    @abstractmethod
    async def get(self):
        raise NotImplementedError


class ArtworkRepository(BaseRepository):
    table = ArtworkTable

    async def create(self, table_entity: ArtworkTable):
        async with self.db.async_session() as session:
            async with session.begin():
                session.add(table_entity)
                return table_entity


    async def list(self):
        query = select(self.table)
        results = await self.execute_query(query)
        return [item for (item,) in results]

    # TODO: Fix
    async def update(self, id: str):
        async with self.db.async_session() as session:
            async with session.begin():
                query = update(self.table).where(self.table.id == id)

    async def delete(self, id: str):
        async with self.db.async_session() as session:
            async with session.begin():
                query = delete(self.table).where(self.table.id == id)
                await self.execute_query(query)
            return True
    
    async def get(self, id: str):
        query = select(self.table).where(self.table.id == id)
        results = await self.execute_query(query)
        for (item,) in results:
            return item
        return None