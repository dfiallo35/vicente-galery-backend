from abc import ABC
from abc import abstractmethod


class BaseMapper(ABC):    
    @abstractmethod
    def entity_to_table(self):
        raise NotImplementedError()
    
    @abstractmethod
    def table_to_entity(self):
        raise NotImplementedError()
