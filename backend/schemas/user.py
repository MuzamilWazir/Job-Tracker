from pydantic import BaseModel
from typing import Optional
from sqlalchemy import DateTime


class UserCreate(BaseModel):
  id : int
  email : str
  hashed_password : str
  created_at : DateTime

class UserOut(BaseModel):
  id : int
  email : str
  created_at : DateTime

  class Config:
    from_attributes = True   # lets Pydantic read data directly from a SQLAlchemy object 