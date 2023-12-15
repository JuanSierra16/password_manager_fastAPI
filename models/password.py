from config.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

class Password(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True)
    userName = Column(String(50), nullable=False)
    userEmail = Column(String, nullable=False)
    password = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)