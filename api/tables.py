import uuid
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID


class BaseTable(DeclarativeBase):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class ArtworkTable(BaseTable):
    __tablename__ = "artworks"
    title: str = Column(String(100))
    description: str = Column(String(500))
