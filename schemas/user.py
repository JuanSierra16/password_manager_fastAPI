from pydantic import BaseModel, Field
from typing import Optional

""" class User(BaseModel):
    id: Optional[int] = None
    username: str = Field(min_length=1, max_length=50)
    email: str = Field(min_length=1, max_length=255)
    hashed_password: str = Field(min_length=1, max_length=255)
    disabled: Optional[bool] = None """

class User(BaseModel):
    username: str
    email: str | None = None
    password: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str