import inject
from galery_api.infrastructure.postgres.repositories import ArtworkRepository
from galery_api.infrastructure.postgres.mappers import ArtworkDataBaseMapper

from core.application.services import BaseService
from core.infrastructure.postgres.repositories import IBaseRepository
from core.infrastructure.postgres.mappers import IBaseMapper


class IArtworkService(BaseService):
    repository: IBaseRepository = inject.attr(ArtworkRepository)
    mapper: IBaseMapper = inject.attr(ArtworkDataBaseMapper)


class ArtworkService(IArtworkService):
    pass
