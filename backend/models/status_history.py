from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import base

class StatusHistory(base):
    __tablename__ = "status_history"

    id = Column(Integer, primary_key=True, index=True)
    old_status = Column(String, nullable=True)
    new_status = Column(String, nullable=False)
    changed_at = Column(DateTime, default=datetime.utcnow)
    application_id = Column(Integer, ForeignKey("applications.id"))

    application = relationship("Application", back_populates="status_history")