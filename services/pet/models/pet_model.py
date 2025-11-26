from pydantic import BaseModel, field_validator, HttpUrl


class Tags(BaseModel):

    id: int
    name: str


class Category(BaseModel):

    id: int
    name: str


class PetModel(BaseModel):

    id: int
    category: Category
    name: str
    photoUrls: list[HttpUrl]
    tags: list[Tags]
    status: str

