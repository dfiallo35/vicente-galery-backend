from galery_api.presentation.api import router
from galery_api.settings import settings

from core.presentation.app import BaseApp

base_app = BaseApp(router=router, settings=settings)
app = base_app.app
