
from typing import List

from abc import ABC
from abc import abstractmethod

from api.models import Artwork
from api.mappers import ArtworkMapper
from api.repositories import ArtworkRepository


class IBaseService(ABC):
    @abstractmethod
    async def create(self):
        raise NotImplementedError
    
    @abstractmethod
    async def delete(self):
        raise NotImplementedError
    
    @abstractmethod
    async def update(self):
        raise NotImplementedError
    
    @abstractmethod
    async def get(self):
        raise NotImplementedError
    
    @abstractmethod
    async def list(self):
        raise NotImplementedError


class InMemoryService(IBaseService):
    data: List[Artwork]

    def __init__(self):
        self.data = []
    
    async def create(self, artwork: Artwork) -> Artwork:
        id = len(self.data) + 1
        artwork.id = id
        self.data.append(artwork)
        return artwork

    async def delete(self, id: int) -> None:
        self.data = [artwork for artwork in self.data if artwork.id != id]
    
    async def update(self, id: int, artwork: Artwork) -> Artwork:
        for i, artwork in enumerate(self.data):
            if artwork.id == id:
                self.data[i] = artwork
                return self.data[i]
    
    async def get(self, id: int) -> Artwork:
        for artwork in self.data:
            if artwork.id == id:
                return artwork
    
    async def list(self) -> List[Artwork]:
        return self.data


class PostgresService(IBaseService):
    repository: ArtworkRepository
    mapper: ArtworkMapper

    def __init__(self):
        self.repository = ArtworkRepository()
        self.mapper = ArtworkMapper()

    async def create(self, artwork: Artwork) -> Artwork:
        artwork_table = self.mapper.entity_to_table(artwork)
        result = await self.repository.create(artwork_table)
        return self.mapper.table_to_entity(result)
    
    async def delete(self, id: str) -> None:
        result = await self.repository.delete(id)
        return result
    
    async def update(self, id: str, artwork: Artwork) -> Artwork:
        ...
    
    async def get(self, id: str) -> Artwork | None:
        result = await self.repository.get(id)
        if result:
            return self.mapper.table_to_entity(result)
        return None

    async def list(self) -> List[Artwork]:
        results = await self.repository.list()
        return [self.mapper.table_to_entity(artwork) for artwork in results]
