from pydantic import BaseModel, ConfigDict
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
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    website: Optional[str]
    notes: Optional[str]
    user_id: int 