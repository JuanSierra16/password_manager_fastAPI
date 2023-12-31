from pydantic import BaseModel, Field, validator
from typing import Optional
import datetime

class Password(BaseModel):
    id: Optional[int] = None
    userName: str = Field(min_length=1, max_length=50)
    userEmail: str = Field(min_length=1, max_length=255)
    creation_date: datetime.datetime
    length: int = Field(ge=8, le=64)
    num_numbers: int = Field(ge=1, le=10)
    num_uppercase: int = Field(ge=1, le=10)
    num_special: int = Field(ge=1, le=10)

    @validator('creation_date', pre=True, always=True)
    def set_creation_date(cls, v):
        return v if v is not None else datetime.datetime.now()