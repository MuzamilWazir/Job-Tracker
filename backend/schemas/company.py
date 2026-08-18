from pydantic import BaseModel
from typing import Optional

# DTO for what the client SENDS when creating a company
class CompanyCreate(BaseModel):
    name: str
    website: Optional[str] = None
    notes: Optional[str] = None

# DTO for what the client SENDS when updating a company (all fields optional)
class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    notes: Optional[str] = None

# DTO for what the server SENDS BACK to the client
class CompanyOut(BaseModel):
    id: int
    name: str
    website: Optional[str]
    notes: Optional[str]
    user_id: int

    class Config:
        from_attributes = True   # lets Pydantic read data directly from a SQLAlchemy object