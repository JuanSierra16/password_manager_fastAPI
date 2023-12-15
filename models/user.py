from config.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    password = Column(String, nullable=False)