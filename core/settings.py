from typing import Dict

import inject
from inject import Binder
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DEPENDENCIES: Dict
    
    def configure(self, binder: Binder):
        for interface, implementation in self.DEPENDENCIES.items():
            binder.bind(interface, implementation())

    def setup(self):
        inject.configure(self.configure)
