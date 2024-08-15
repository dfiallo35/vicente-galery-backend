import inject
from inject import Binder

from api.services import IBaseService
from api.services import InMemoryService


DEPENDENCIES = {
    IBaseService: InMemoryService
}


def configure(binder: Binder):
    for interface, implementation in DEPENDENCIES.items():
        binder.bind(interface, implementation())

inject.configure(configure)