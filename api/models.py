from pydantic import BaseModel

from typing import Optional


class Artwork(BaseModel):
    id: Optional[int] = None
    title: str
    description: str


class ArtworkInput(BaseModel):
    title: str
    description: str


class ArtworkOutput(BaseModel):
    id: int
    title: str
    description: str
