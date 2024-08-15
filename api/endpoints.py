import inject
from fastapi import FastAPI
from fastapi import status

from api.services import IBaseService
from api.services import InMemoryService
from api.models import ArtworkInput
from api.models import ArtworkOutput
from api.mappers import ArtworkMapper


app = FastAPI()
service: IBaseService = inject.instance(IBaseService)


@app.get("/")
async def heatlh_check():
    return {"message": "OK"}


@app.post(
    "/artwork",
    responses={
        status.HTTP_201_CREATED: {"model": ArtworkOutput},
    }
)
async def create_artwork(artwork: ArtworkInput):
    mapper = ArtworkMapper()
    artwork_entity = mapper.to_entity(artwork)
    artwork_entity = await service.create(artwork_entity)
    return mapper.to_api(artwork_entity)
