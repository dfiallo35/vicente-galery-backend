from galery_api.presentation.api import router

from core.presentation.app import create_app


app = create_app(router=router)
