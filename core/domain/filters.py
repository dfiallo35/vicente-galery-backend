from pydantic import BaseModel


class IBaseFilter(BaseModel):
    pass


class IPaginationBaseFilter(IBaseFilter):
    page: int = 1
    size: int = 10
    order_by: str = None

    @property
    def offset(self):
        return (self.page - 1) * self.size

    @property
    def limit(self):
        return self.size
