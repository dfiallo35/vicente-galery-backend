from abc import ABC
from abc import abstractmethod

from api.models import Artwork
from api.models import ArtworkInput
from api.models import ArtworkOutput


class BaseMapper(ABC):
    @abstractmethod
    def to_entity(self):
        raise NotImplementedError

    @abstractmethod
    def to_api(self):
        raise NotImplementedError


class ArtworkMapper(BaseMapper):
    def to_entity(self, artwork_input: ArtworkInput) -> Artwork:
        return Artwork(title=artwork_input.title, description=artwork_input.description)

    def to_api(self, artwork: Artwork) -> ArtworkOutput:
        return ArtworkOutput(id=artwork.id, title=artwork.title, description=artwork.description)
