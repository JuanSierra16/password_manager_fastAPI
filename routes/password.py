from fastapi import APIRouter
from schemas.password import Password
from typing import List
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

password_router = APIRouter()

@password_router.get("/password", tags=['password'], response_model = List[Password], status_code=200)
def get_passwords() -> List[Password]:
    db = Session()
    result = db.query(Password).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))