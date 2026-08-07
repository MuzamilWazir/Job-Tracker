from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import base

class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # This isn't a real column — it's SQLAlchemy's way of saying
    # "give me easy access to all companies/applications this user owns"
    companies = relationship("Company", back_populates="owner")
    applications = relationship("Application", back_populates="owner")