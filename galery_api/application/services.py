from galery_api.infrastructure.postgres.repositories import ArtworkRepository
from galery_api.infrastructure.postgres.mappers import ArtworkDataBaseMapper

from core.application.services import SqlService


class ArtworkService(SqlService):
    repository = ArtworkRepository
    mapper = ArtworkDataBaseMapper
