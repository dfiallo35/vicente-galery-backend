from galery_api.application.services import ArtworkService
from galery_api.application.services import IArtworkService
from galery_api.infrastructure.postgres.repositories import IArtworkRepository
from galery_api.infrastructure.postgres.repositories import ArtworkRepository

from core.settings import Settings


DEPENDENCIES = {
    IArtworkRepository: ArtworkRepository,
    IArtworkService: ArtworkService
}

settings = Settings(DEPENDENCIES=DEPENDENCIES)
