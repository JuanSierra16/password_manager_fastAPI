from fastapi import APIRouter, Path, Depends
from schemas.password import Password
from typing import List
from config.database import Session
from models.password import Password as PasswordModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer

password_router = APIRouter()

@password_router.get("/passwords", tags=['passwords'], response_model = List[Password], status_code=200, dependencies=[Depends(JWTBearer())])
def get_passwords() -> List[Password]:
    db = Session()
    result = db.query(PasswordModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@password_router.get("/passwords/{id}", tags=['passwords'], response_model = Password, status_code=200)
def get_password(id: int = Path(ge=1, le=2000)):
    db = Session()
    result = db.query(PasswordModel).filter(PasswordModel.id == id).first()
    if result:
        response = JSONResponse(status_code=200, content=jsonable_encoder(result))
    else:
        response = JSONResponse(status_code=404, content={"message": "Password not found"})
    return response

@password_router.post("/passwords", tags=['passwords'], response_model = List[Password], status_code=201)
def create_password(password: Password):
    db = Session()
    new_password = PasswordModel(**password.model_dump())
    db.add(new_password)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Password created successfully"})

@password_router.put("/passwords/{id}", tags=['passwords'], response_model = dict, status_code=200)
def update_password(id: int, password: Password):
    db = Session()
    result = db.query(PasswordModel).filter(PasswordModel.id == id).first()
    if result:
        result.userName = password.userName
        result.userEmail = password.userEmail
        result.password = password.password
        result.creation_date = password.creation_date
        db.commit()
        response = JSONResponse(status_code=200, content={"message": "Password updated successfully"})
    else:
        response = JSONResponse(status_code=404, content={"message": "Password not found"})
    return response

@password_router.delete("/passwords/{id}", tags=['passwords'], response_model = dict, status_code=200)
def delete_password(id: int):
    db = Session()
    result = db.query(PasswordModel).filter(PasswordModel.id == id).first()
    if result:
        db.delete(result)
        db.commit()
        response = JSONResponse(status_code=200, content={"message": "Password deleted successfully"})
    else:
        response = JSONResponse(status_code=404, content={"message": "Password not found"})
    return response