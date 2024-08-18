from fastapi.routing import APIRouter
from api.endpoints import router as artwork_router


api_router = APIRouter()
api_router.include_router(artwork_router, prefix="/artwork")

@api_router.get("/")
async def health():
    return {"status": "ok"}
