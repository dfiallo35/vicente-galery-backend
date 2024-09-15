import inject
from typing import List
from fastapi.routing import APIRouter
from fastapi import status
from fastapi import Response

from api.services import IBaseService
from api.models import ArtworkInput
from api.models import ArtworkOutput
from api.mappers import ArtworkMapper


router = APIRouter()
service: IBaseService = inject.instance(IBaseService)


@router.post(
    "/",
    responses={
        status.HTTP_201_CREATED: {"model": ArtworkOutput},
    }
)
async def create_artwork(artwork: ArtworkInput):
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
    result = await service.delete(id)
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"details": f"Artwork with id \"{id}\" not found"}
    response.status_code = status.HTTP_204_NO_CONTENT
