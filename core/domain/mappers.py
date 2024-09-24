from abc import ABC
from abc import abstractmethod


class IBaseMapper(ABC):
    @abstractmethod
    async def api_to_entity(self):
        raise NotImplementedError()

    @abstractmethod
    async def entity_to_api(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def model_dump(self):
        raise NotImplementedError()
