from galery_api.application.services import IBaseService
from galery_api.application.services import PostgresService

from core.settings import Settings


DEPENDENCIES = {
    IBaseService: PostgresService
}

settings = Settings(DEPENDENCIES=DEPENDENCIES)
