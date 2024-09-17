from typing import Optional
from pydantic import BaseModel


# generic base model 
class BaseEntity(BaseModel):
    id: Optional[str] = None


class BaseInput(BaseModel):
    pass


class BaseOutput(BaseModel):
    pass
