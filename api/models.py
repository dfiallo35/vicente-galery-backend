from typing import Optional

from pydantic import BaseModel


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
