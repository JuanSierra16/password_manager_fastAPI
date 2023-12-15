from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import create_token, validate_token
from config.database import Session
from models.user import User as UserModel

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        db = Session()
        result = db.query(UserModel).filter(UserModel.email == data['email']).first()
        if not result:
            raise HTTPException(status_code=401, detail="Invalid user")