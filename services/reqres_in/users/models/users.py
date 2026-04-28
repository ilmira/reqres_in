from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, HttpUrl


class Support(BaseModel):
    url: HttpUrl
    text: str


class UserItem(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

class Meta(BaseModel):
    powered_by: str
    upgrade_url: HttpUrl
    docs_url: HttpUrl
    template_gallery: HttpUrl
    message: str
    features: List[str]
    upgrade_cta: str

class UserData(BaseModel):
    data: UserItem
    support: Support
    _meta: Meta


class SingleUserResponse(BaseModel):
    data: UserItem
    support: Support


class CreateUserRequest(BaseModel):
    name: str
    job: str


class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime


class UpdateUserRequest(BaseModel):
    name: Optional[str] = None
    job: Optional[str] = None


class UpdateUserResponse(BaseModel):
    name: Optional[str]
    job: Optional[str]
    updatedAt: datetime

class UsersListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserItem]
    support: Support
    _meta: dict
