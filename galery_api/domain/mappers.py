from galery_api.domain.models import Artwork
from galery_api.domain.models import ArtworkInput
from galery_api.domain.models import ArtworkUpdate
from galery_api.domain.models import ArtworkOutput

from core.domain.mappers import BaseMapper


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

    def model_dump(self, artwork_update: ArtworkUpdate) -> dict:
        return artwork_update.model_dump(exclude_none=True)
