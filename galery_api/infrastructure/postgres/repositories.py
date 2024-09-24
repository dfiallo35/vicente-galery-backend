import inject

from galery_api.infrastructure.postgres.tables import ArtworkTable
from galery_api.infrastructure.postgres.mappers import ArtworkFilterMapper

from core.infrastructure.postgres.repositories import BaseRepository
from core.infrastructure.postgres.mappers import IBaseFilterMapper


class IArtworkRepository(BaseRepository):
    table_class = ArtworkTable
    filter_mapper: IBaseFilterMapper = inject.attr(ArtworkFilterMapper)


class ArtworkRepository(IArtworkRepository):
    pass
