from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import base

class Application(base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String, nullable=False)
    status = Column(String, default="applied")
    applied_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String, nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    company = relationship("Company", back_populates="applications")
    owner = relationship("User", back_populates="applications")
    status_history = relationship("StatusHistory", back_populates="application")