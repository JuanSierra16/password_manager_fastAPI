from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class Password(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    userName = Column(String(50), nullable=False)
    userEmail = Column(String, nullable=False)
    password = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
    # Relación con la tabla 'users'
    user = relationship("User", back_populates="passwords")