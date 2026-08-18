from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from auth.hashing import hash_password , verify_password
from backend.auth.jwt_handler import create_access_token
from database import get_db
from models.user import User

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


def login_user(email : str , password : str, db : Session):
   user_exist = db.query(User).filter(User.email == email).first()
   if not user_exist:
        raise HTTPException(401, detail =  "User not existed")

   
   hash_pw = user_exist.hashed_password 
   correctPassword = verify_password(password , hash_pw)
   if not correctPassword:
        raise HTTPException(401, detail =  "Invalid password")




