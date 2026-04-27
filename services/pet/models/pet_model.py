from pydantic import BaseModel
from typing import Optional
from enum import Enum


class Tags(BaseModel):

    id: Optional[int] = None
    name: Optional[str] = None


class Category(BaseModel):

    id: Optional[int] = None
    name: Optional[str] = None


class PetStatus(str, Enum):

    available = "available"
    pending = "pending"
    sold = "sold"


class PetModel(BaseModel):

    id: Optional[int] = None
    category: Optional[Category] = None
    name: str
    photoUrls:  list[str]
    tags: Optional[list[Tags]] = None
    status: Optional[PetStatus] = None


class ApiResponseModel(BaseModel):

    code: int
    type: str
    message: str

