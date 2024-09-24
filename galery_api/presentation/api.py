import inject
from typing import List
from typing import Annotated
from fastapi import Query
from fastapi import status
from fastapi import Response
from fastapi.routing import APIRouter

from galery_api.domain.models import ArtworkInput
from galery_api.domain.models import ArtworkUpdate
from galery_api.domain.models import ArtworkOutput
from galery_api.domain.mappers import ArtworkMapper
from galery_api.domain.filters import ArtworkFilter
from galery_api.application.services import IArtworkService


router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post(
    "/artwork",
    responses={
        status.HTTP_201_CREATED: {"model": ArtworkOutput},
    }
)
async def create_artwork(artwork: ArtworkInput):
    service: IArtworkService = inject.instance(IArtworkService)
    mapper = ArtworkMapper()
    artwork_entity = await mapper.api_to_entity(artwork)
    artwork_entity = await service.create(artwork_entity)
    return await mapper.entity_to_api(artwork_entity)


@router.get(
    "/artwork",
    responses={
        status.HTTP_200_OK: {"model": List[ArtworkOutput]},
    }
)
async def list_artwork(filter_query: Annotated[ArtworkFilter, Query()]):
    service: IArtworkService = inject.instance(IArtworkService)
    mapper = ArtworkMapper()
    artworks = await service.list(filter_query=filter_query)
    return [await mapper.entity_to_api(artwork) for artwork in artworks]


@router.get(
    "/artwork/{id}",
    responses={
        status.HTTP_200_OK: {"model": ArtworkOutput},
        status.HTTP_404_NOT_FOUND: {}
    }
)
async def get_artwork(id: str, response: Response):
    service: IArtworkService = inject.instance(IArtworkService)
    mapper = ArtworkMapper()
    artwork = await service.get(id)
    if not artwork:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"details": f"Artwork with id \"{id}\" not found"}
    return await mapper.entity_to_api(artwork)


@router.patch(
    "/artwork/{id}",
    responses={
        status.HTTP_200_OK: {"model": ArtworkOutput},
    }
)
async def update_artwork(id: str, artwork: ArtworkUpdate):
    service: IArtworkService = inject.instance(IArtworkService)
    mapper = ArtworkMapper()
    changes = await mapper.model_dump(artwork)
    artwork_entity = await service.update(id, changes)
    return await mapper.entity_to_api(artwork_entity)


@router.delete(
    "/artwork/{id}",
    responses={
        status.HTTP_200_OK: {"model": None},
    }
)
async def delete_artwork(id: str, response: Response):
    service: IArtworkService = inject.instance(IArtworkService)
    result = await service.delete(id)
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"details": f"Artwork with id \"{id}\" not found"}
    response.status_code = status.HTTP_204_NO_CONTENT
