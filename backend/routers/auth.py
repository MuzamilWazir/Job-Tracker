from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.user import create_user, login_user
from schemas.user import UserCreate
from database import get_db


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register_user(body: UserCreate, db: Session = Depends(get_db)):
    return create_user(body.email, body.password, db)


@router.post("/login")
def login(body: UserCreate, db: Session = Depends(get_db)):
    return login_user(body.email, body.password, db)
