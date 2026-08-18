from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
  email : str
  password : str

class UserOut(BaseModel):
  id : int
  email : str
  created_at : datetime

  class Config:
    from_attributes = True