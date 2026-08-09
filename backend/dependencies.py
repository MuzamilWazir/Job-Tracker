from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from database import SessionLocal
from model.user import User
from config import settings

# This tells FastAPI: "expect a Bearer token in the Authorization header,
# and the login endpoint that issues tokens is at /auth/login"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


# Gives every request a fresh DB session, and closes it afterward
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Decodes the JWT token, finds the matching user in the DB, returns it
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception

    return user