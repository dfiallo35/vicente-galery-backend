from abc import ABC
from abc import abstractmethod
from decouple import config
from typing import List
from typing import Dict

from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy import update

# TODO: fix db connection
from core.infrastructure.postgres.database import DataBase
from core.infrastructure.postgres.tables import BaseTable
from core.domain.filters import IBaseFilter
from core.domain.filters import IPaginationBaseFilter
from core.infrastructure.postgres.mappers import IBaseFilterMapper


DATABASE_URL = config("DATABASE_URL", "")


class IBaseRepository(ABC):
    table_class: BaseTable = None
    filter_mapper: IBaseFilterMapper = None

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
    
    async def get_conditions(self, filter_query: IBaseFilter):
        conditions = await self.filter_mapper.filter_to_conditions(filter_query)
        return conditions
    
    async def build_query(self, conditions: List):
        query = select(self.table_class)
        for condition in conditions:
            query = query.where(condition)
        return query
    
    async def get_items(self, results):
        return [item for (item,) in results]

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


class BaseRepository(IBaseRepository):
    async def create(self, table_entity: BaseTable):
        async with self.db.async_session() as session:
            async with session.begin():
                session.add(table_entity)
                return table_entity

    async def list(self, filter_query: IBaseFilter):
        conditions = await self.get_conditions(filter_query)
        query = await self.build_query(conditions)
        results = await self.execute_query(query)
        return await self.get_items(results)
    
    # TODO: Fix adding pagination class, total, page and size info
    async def paginate(self, filter_query: IPaginationBaseFilter):
        conditions = await self.get_conditions(filter_query)
        query = await self.build_query(conditions)
        query = query.limit(filter_query.limit).offset(filter_query.offset)
        results = await self.execute_query(query)
        return await self.get_items(results)

    async def update(self, id: str, changes: Dict):
        async with self.db.async_session() as session:
            async with session.begin():
                query = update(self.table_class).where(self.table_class.id == id).values(**changes)
                await self.execute_query(query)
                query = select(self.table_class).where(self.table_class.id == id)
                results = await self.execute_query(query)
                items = await self.get_items(results)
                if items:
                    return items[0]
                return None

    async def delete(self, id: str):
        async with self.db.async_session() as session:
            async with session.begin():
                query = delete(self.table_class).where(self.table_class.id == id)
                await self.execute_query(query)
            return True
    
    async def get(self, id: str):
        query = select(self.table_class).where(self.table_class.id == id)
        results = await self.execute_query(query)
        items = await self.get_items(results)
        if items:
            return items[0]
        return None
