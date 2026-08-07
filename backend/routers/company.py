from sqlalchemy import APIRouter , Depends

from backend import crud


router = APIRouter()

@router.post("/create")
def create_company():
    return crud.create_company()