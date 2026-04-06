from pydantic import BaseModel, field_validator
from typing import Optional


class UserModel(BaseModel):

    id: Optional[int] = None
    username: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    userStatus: Optional[int] = None


class ApiResponseModel(BaseModel):

    code: int
    type: str
    message: str




