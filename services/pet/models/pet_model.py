from pydantic import BaseModel, field_validator, HttpUrl
from typing import Optional, List


class Tags(BaseModel):

    id: Optional[int] = None
    name: Optional[str] = None


class Category(BaseModel):

    id: Optional[int] = None
    name: Optional[str] = None


class PetModel(BaseModel):

    id: Optional[int] = None
    category: Optional[Category] = None
    name: str
    photoUrls:  list[str]
    tags: Optional[list[Tags]] = None
    status: Optional[str] = None


class ApiResponseModel(BaseModel):

    code: int
    type: str
    message: str

