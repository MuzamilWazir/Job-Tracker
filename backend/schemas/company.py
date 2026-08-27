from pydantic import BaseModel
from typing import Optional


class CompanyCreate(BaseModel):
    name: str
    website: Optional[str] = None
    notes: Optional[str] = None


class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    notes: Optional[str] = None

class CompanyOut(BaseModel):
    id: int
    name: str
    website: Optional[str]
    notes: Optional[str]
    user_id: int

    class Config:
        from_attributes = True   