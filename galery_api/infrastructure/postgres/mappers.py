from galery_api.domain.models import Artwork
from galery_api.domain.filters import ArtworkFilter
from galery_api.infrastructure.postgres.tables import ArtworkTable

from core.infrastructure.postgres.mappers import IBaseMapper
from core.infrastructure.postgres.mappers import IBaseFilterMapper


class ArtworkDataBaseMapper(IBaseMapper):
    async def entity_to_table(self, artwork: Artwork) -> ArtworkTable:
        return ArtworkTable(
            id=artwork.id,
            title=artwork.title,
            description=artwork.description
        )
    
    async def table_to_entity(self, artwork_table: ArtworkTable) -> Artwork:
        return Artwork(
            id=str(artwork_table.id),
            title=artwork_table.title,
            description=artwork_table.description
        )


class ArtworkFilterMapper(IBaseFilterMapper):
    async def filter_to_conditions(self, filter_query: ArtworkFilter) -> list:
        conditions = []
        if filter_query.entity_ids:
            conditions.append(ArtworkTable.id.in_(filter_query.entity_ids))
        
        if filter_query.keyword:
            conditions.append(ArtworkTable.title.ilike(f"%{filter_query.keyword}%"))
        
        return conditions
