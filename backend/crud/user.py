from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from auth.hashing import hash_password , verify_password
from database import get_db
from model.user import User

def create_user(email : str , password : str, db : Session):
   existing_user = db.query(User).filter(User.email == email).first()
   if existing_user:
     raise HTTPException(409, detail =  "User already existed")

   hash_pw =  hash_password(password)

   new_user = User(
    email=email,
    hashed_password=hash_pw)
   db.add(new_user)
   db.commit()
   db.refresh(new_user)
   return new_user