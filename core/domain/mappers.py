from abc import ABC
from abc import abstractmethod


class BaseMapper(ABC):
    @abstractmethod
    def api_to_entity(self):
        raise NotImplementedError()

    @abstractmethod
    def entity_to_api(self):
        raise NotImplementedError()
    
    @abstractmethod
    def model_dump(self):
        raise NotImplementedError()
