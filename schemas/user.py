from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    email: str = Field(min_length=1, max_length=255)
    password: str = Field(min_length=1, max_length=255)