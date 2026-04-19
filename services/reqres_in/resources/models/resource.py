from typing import List
from pydantic import BaseModel

class Support(BaseModel):
    url: str
    text: str

class ResourceData(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class SingleResourceResponse(BaseModel):
    data: ResourceData
    support: Support
    _meta: dict


class ResourcesListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[ResourceData]
    support: Support
    _meta: dict
