from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class ApplicationCreate(BaseModel):
    job_title: str
    notes: Optional[str] = None
    company_id: int = Field(..., description="The ID of the company this application is for")


class ApplicationUpdate(BaseModel):
    job_title: Optional[str] = None
    notes: Optional[str] = None


class ApplicationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    job_title: str
    status: str
    applied_date: datetime
    notes: Optional[str]
    company_id: int
    user_id: int