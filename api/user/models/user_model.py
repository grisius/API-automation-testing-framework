from pydantic import BaseModel


class UserModel(BaseModel):

    id: int | None = None
    username: str
    firstName: str | None = None
    lastName: str | None = None
    email: str | None = None
    password: str
    phone: str | None = None
    userStatus: int | None = None


class ApiResponseModel(BaseModel):

    code: int
    type: str
    message: str




