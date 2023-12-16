from fastapi import APIRouter, Path, Depends
from schemas.password import Password
from typing import List
from config.database import Session
from models.password import Password as PasswordModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from utils.authentication import get_current_active_user
from schemas.user import User
from fastapi import HTTPException
from utils.session import get_db
from utils.random_password import generate_random_password
from schemas.password_response import PasswordResponse

password_router = APIRouter()

@password_router.get("/passwords", tags=['passwords'], response_model=List[PasswordResponse], status_code=200)
def get_passwords(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthenticated user")

    # Filtrar las contraseñas del usuario activo
    user_passwords = db.query(PasswordModel).filter(PasswordModel.user_id == current_user.id).all()
    return user_passwords

@password_router.get("/passwords/{id}", tags=['passwords'], response_model = Password, status_code=200)
def get_password(id: int = Path(ge=1, le=2000)):
    db = Session()
    result = db.query(PasswordModel).filter(PasswordModel.id == id).first()
    if result:
        response = JSONResponse(status_code=200, content=jsonable_encoder(result))
    else:
        response = JSONResponse(status_code=404, content={"message": "Password not found"})
    return response

@password_router.post("/passwords", tags=['passwords'], response_model=Password, status_code=201)
def create_password(password: Password, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthenticated user")

    # Genera una contraseña aleatoria basada en los parámetros proporcionados por el usuario
    random_password = generate_random_password(password.length, password.num_numbers, password.num_uppercase, password.num_special)

    # Crea una nueva contraseña asociada al usuario actual
    new_password = PasswordModel(userName=password.userName, userEmail=password.userEmail, password=random_password, user_id=current_user.id)
    db.add(new_password)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Password created successfully", "password": random_password})

@password_router.put("/passwords/{id}", tags=['passwords'], response_model = dict, status_code=200)
def update_password(id: int, password: Password, current_user: User = Depends(get_current_active_user)):
    db = Session()
    result = db.query(PasswordModel).filter(PasswordModel.id == id).first()
    if result:
        if result.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized to update this password")
        result.userName = password.userName
        result.userEmail = password.userEmail

        # Genera una nueva contraseña aleatoria basada en los parámetros proporcionados por el usuario
        new_password = generate_random_password(password.length, password.num_numbers, password.num_uppercase, password.num_special)
        result.password = new_password

        result.creation_date = password.creation_date
        db.commit()
        response = JSONResponse(status_code=200, content={"message": "Password updated successfully", "password": new_password})
    else:
        response = JSONResponse(status_code=404, content={"message": "Password not found"})
    return response

@password_router.delete("/passwords/{id}", tags=['passwords'], response_model = dict, status_code=200)
def delete_password(id: int, current_user: User = Depends(get_current_active_user)):
    db = Session()
    result = db.query(PasswordModel).filter(PasswordModel.id == id).first()
    if result:
        if result.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized to delete this password")
        db.delete(result)
        db.commit()
        response = JSONResponse(status_code=200, content={"message": "Password deleted successfully"})
    else:
        response = JSONResponse(status_code=404, content={"message": "Password not found"})
    return response