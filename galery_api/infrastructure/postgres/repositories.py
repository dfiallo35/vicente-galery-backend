from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy import update

from galery_api.infrastructure.postgres.tables import ArtworkTable

from core.infrastructure.postgres.repositories import BaseRepository


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
