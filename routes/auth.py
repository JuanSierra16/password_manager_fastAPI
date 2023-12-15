from schemas.user import User
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from fastapi import APIRouter
from config.database import Session
from models.user import User as UserModel

auth_router = APIRouter()

@auth_router.post("/login", tags=['auth'], response_model = dict, status_code=200)
def login(user: User):
    db = Session()
    result = db.query(UserModel).filter(UserModel.email == user.email, UserModel.password == user.password).first()
    if result:
        token = create_token(data=user.model_dump())
        result = JSONResponse(content={"token": token}, status_code=200)
    else:
        result = JSONResponse(content={"message": "Invalid credentials"}, status_code=401)
    return result

@auth_router.post("/register", tags=['auth'], response_model = dict, status_code=200)
def register(user: User):
    db = Session()
    new_user = UserModel(**user.model_dump())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "User created successfully"})