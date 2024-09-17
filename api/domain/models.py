from core.domain.models import BaseEntity


class Artwork(BaseEntity):
    title: str
    description: str


class ArtworkInput(BaseEntity):
    title: str
    description: str


class ArtworkOutput(BaseEntity):
    id: str
    title: str
    description: str
