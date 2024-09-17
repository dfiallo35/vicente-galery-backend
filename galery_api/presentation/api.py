import inject
from typing import List
from fastapi.routing import APIRouter
from fastapi import status
from fastapi import Response

from galery_api.application.services import IBaseService
from galery_api.domain.models import ArtworkInput
from galery_api.domain.models import ArtworkOutput
from galery_api.domain.mappers import ArtworkMapper


router = APIRouter(prefix="/artwork")


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post(
    "/",
    responses={
        status.HTTP_201_CREATED: {"model": ArtworkOutput},
    }
)
async def create_artwork(artwork: ArtworkInput):
    service: IBaseService = inject.instance(IBaseService)
    mapper = ArtworkMapper()
    artwork_entity = mapper.api_to_entity(artwork)
    artwork_entity = await service.create(artwork_entity)
    return mapper.entity_to_api(artwork_entity)


@router.get(
    "/",
    responses={
        status.HTTP_200_OK: {"model": List[ArtworkOutput]},
    }
)
async def list_artwork():
    service: IBaseService = inject.instance(IBaseService)
    mapper = ArtworkMapper()
    artworks = await service.list()
    return [mapper.entity_to_api(artwork) for artwork in artworks]


@router.get(
    "/{id}",
    responses={
        status.HTTP_200_OK: {"model": ArtworkOutput},
        status.HTTP_404_NOT_FOUND: {}
    }
)
async def get_artwork(id: str, response: Response):
    service: IBaseService = inject.instance(IBaseService)
    mapper = ArtworkMapper()
    artwork = await service.get(id)
    if not artwork:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"details": f"Artwork with id \"{id}\" not found"}
    return mapper.entity_to_api(artwork)


@router.patch(
    "/{id}",
    responses={
        status.HTTP_200_OK: {"model": ArtworkOutput},
    }
)
async def update_artwork(id: str, artwork: ArtworkInput):
    service: IBaseService = inject.instance(IBaseService)
    mapper = ArtworkMapper()
    artwork_entity = mapper.api_to_entity(artwork)
    artwork_entity = await service.update(id, artwork_entity)
    return mapper.entity_to_api(artwork_entity)


@router.delete(
    "/{id}",
    responses={
        status.HTTP_200_OK: {"model": None},
    }
)
async def delete_artwork(id: str, response: Response):
    service: IBaseService = inject.instance(IBaseService)
    result = await service.delete(id)
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"details": f"Artwork with id \"{id}\" not found"}
    response.status_code = status.HTTP_204_NO_CONTENT
