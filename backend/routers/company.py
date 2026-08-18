from fastapi import APIRouter, Depends

from crud import company
from database import get_db
from schemas.company import CompanyCreate


router = APIRouter()

@router.post("/create")
def create_company(company: CompanyCreate , db=Depends(get_db)):
    return company.create_company(company=company , db=db)