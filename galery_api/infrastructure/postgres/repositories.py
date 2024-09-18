from galery_api.infrastructure.postgres.tables import ArtworkTable
from galery_api.infrastructure.postgres.mappers import ArtworkFilterMapper

from core.infrastructure.postgres.repositories import BaseRepository


class ArtworkRepository(BaseRepository):
    table = ArtworkTable
    filter_mapper = ArtworkFilterMapper
