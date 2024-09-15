from abc import ABC
from abc import abstractmethod

from api.models import Artwork
from api.models import ArtworkInput
from api.models import ArtworkOutput
from api.tables import ArtworkTable


class BaseMapper(ABC):
    @abstractmethod
    def api_to_entity(self):
        raise NotImplementedError

    @abstractmethod
    def entity_to_api(self):
        raise NotImplementedError
    
    @abstractmethod
    def entity_to_table(self):
        raise NotImplementedError
    
    @abstractmethod
    def table_to_entity(self):
        raise NotImplementedError


class ArtworkMapper(BaseMapper):
    def api_to_entity(self, artwork_input: ArtworkInput) -> Artwork:
        return Artwork(
            title=artwork_input.title,
            description=artwork_input.description
        )

    def entity_to_api(self, artwork: Artwork) -> ArtworkOutput:
        return ArtworkOutput(
            id=artwork.id,
            title=artwork.title,
            description=artwork.description
        )

    def entity_to_table(self, artwork: Artwork) -> ArtworkTable:
        return ArtworkTable(
            id=artwork.id,
            title=artwork.title,
            description=artwork.description
        )
    
    def table_to_entity(self, artwork_table: ArtworkTable) -> Artwork:
        return Artwork(
            id=str(artwork_table.id),
            title=artwork_table.title,
            description=artwork_table.description
        )
