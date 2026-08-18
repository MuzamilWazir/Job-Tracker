from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from auth.hashing import hash_password , verify_password
from auth.jwt_handler import create_access_token
from database import get_db
from models.user import User

def create_user(email : str , password : str, db : Session) -> User:
   existing_user = db.query(User).filter(User.email == email).first()
   if existing_user:
     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail =  "User already existed")

   hash_pw =  hash_password(password)

   new_user = User(
    email=email,
    hashed_password=hash_pw)
   db.add(new_user)
   db.commit()
   db.refresh(new_user)
   return new_user


def login_user(email : str , password : str, db : Session) -> dict:
   user = db.query(User).filter(User.email == email).first()
   if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =  "User not existed")

   correctPassword = verify_password(password , user.hashed_password )
   if not correctPassword:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail =  "Invalid password")
   access_token = create_access_token(data={"sub": str(user.id)})
   return {"access_token": access_token, "token_type": "bearer"}




