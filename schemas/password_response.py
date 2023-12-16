from pydantic import BaseModel
import datetime

class PasswordResponse(BaseModel):
    id: int
    userName: str
    userEmail: str
    password: str
    creation_date: datetime.datetime