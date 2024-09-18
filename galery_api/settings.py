from galery_api.application.services import ArtworkService

from core.settings import Settings
from core.application.services import IBaseService


DEPENDENCIES = {
    IBaseService: ArtworkService
}

settings = Settings(DEPENDENCIES=DEPENDENCIES)
