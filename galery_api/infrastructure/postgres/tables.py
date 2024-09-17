from sqlalchemy import Column
from sqlalchemy import String

from core.infrastructure.postgres.tables import BaseTable


class ArtworkTable(BaseTable):
    __tablename__ = "artworks"
    title: str = Column(String(100))
    description: str = Column(String(500))
