from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=None, nullable=True)