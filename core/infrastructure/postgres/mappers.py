from abc import ABC
from abc import abstractmethod
from typing import List

from core.domain.filters import IBaseFilter

class IBaseMapper(ABC):    
    @abstractmethod
    async def entity_to_table(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def table_to_entity(self):
        raise NotImplementedError()


class IBaseFilterMapper(ABC):    
    @abstractmethod
    async def filter_to_conditions(self, filter_query: IBaseFilter) -> List:
        raise NotImplementedError()
