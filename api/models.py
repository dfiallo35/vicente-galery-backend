from typing import Optional

from pydantic import BaseModel


class Artwork(BaseModel):
    id: Optional[str] = None
    title: str
    description: str


class ArtworkInput(BaseModel):
    title: str
    description: str


class ArtworkOutput(BaseModel):
    id: str
    title: str
    description: str
