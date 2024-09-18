from typing import Optional
from typing import List

from core.domain.filters import IPaginationBaseFilter


class ArtworkFilter(IPaginationBaseFilter):
    entity_ids: Optional[List[str]] = None
    keyword: Optional[str] = None
