from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from models.user import User as UserModel
from config.database import Session

from schemas.user import User
from schemas.token import Token
from utils.authentication import authenticate_user, create_access_token, get_password_hash, get_current_active_user
from utils.session import get_db

ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
auth_router = APIRouter()

@auth_router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



@auth_router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@auth_router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]

@auth_router.get("/users", tags=['users'], response_model = List[User], status_code=200)
def get_users() -> List[User]:
    db = Session()
    result = db.query(UserModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@auth_router.post("/users", tags=['users'], response_model = List[User], status_code=201)
def create_user(user: User):
    db = Session()
    hashed_password = get_password_hash(user.password)
    new_user = UserModel(
        username=user.username, 
        email=user.email, 
        hashed_password=hashed_password, 
        disabled=user.disabled)
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Password created successfully"})