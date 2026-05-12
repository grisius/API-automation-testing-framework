from pydantic import BaseModel
from enum import Enum


class Tags(BaseModel):

    id: int | None = None
    name: str | None = None


class Category(BaseModel):

    id: int | None = None
    name: str | None = None


class PetStatus(str, Enum):

    available = "available"
    pending = "pending"
    sold = "sold"


class PetModel(BaseModel):

    id: int | None = None
    category: Category | None = None
    name: str
    photoUrls: list[str]
    tags: list[Tags] | None = None
    status: PetStatus | None = None


class ApiResponseModel(BaseModel):

    code: int
    type: str
    message: str

