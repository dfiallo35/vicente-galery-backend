from api.domain.models import Artwork
from api.infrastructure.postgres.tables import ArtworkTable

from core.infrastructure.postgres.mappers import BaseMapper


class ArtworkDataBaseMapper(BaseMapper):
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
