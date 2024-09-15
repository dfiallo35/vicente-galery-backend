import inject
from inject import Binder
from pydantic_settings import BaseSettings

from api.services import IBaseService
from api.services import PostgresService


DEPENDENCIES = {
    IBaseService: PostgresService
}

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    
    def configure(binder: Binder):
        for interface, implementation in DEPENDENCIES.items():
            binder.bind(interface, implementation())

    inject.configure(configure)


settings = Settings()
