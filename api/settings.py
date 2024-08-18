import inject
from inject import Binder
from inject import Injector

from api.services import IBaseService
from api.services import InMemoryService


DEPENDENCIES = {
    IBaseService: InMemoryService
}


def configure(binder: Binder):
    for interface, implementation in DEPENDENCIES.items():
        binder.bind(interface, implementation())

injector = Injector(configure)
inject.set_injector(injector)
inject.configure(configure)
