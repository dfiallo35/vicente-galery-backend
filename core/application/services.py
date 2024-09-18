from abc import ABC
from abc import abstractmethod

from core.domain.filters import IBaseFilter


class IBaseService(ABC):
    @abstractmethod
    async def create(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def delete(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def update(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def get(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def list(self, filter_query: IBaseFilter):
        raise NotImplementedError()
