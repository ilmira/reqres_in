from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


class Support(BaseModel):
    url: str
    text: str


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class SingleUserResponse(BaseModel):
    data: UserData
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
    data: List[UserData]
    support: Support
    _meta: dict
