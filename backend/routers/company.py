from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies import get_current_user
from models.user import User
from schemas.company import CompanyCreate, CompanyUpdate, CompanyOut
from crud.company import (
    create_company,
    get_companies_by_user,
    get_company,
    update_company,
    delete_company,
)


router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)


@router.post("/", response_model=CompanyOut)
def create_company_endpoint(
    body: CompanyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> CompanyOut:
    """Create a new company owned by the current user."""
    return create_company(db, body, current_user.id)


@router.get("/", response_model=list[CompanyOut])
def get_companies_endpoint(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> list[CompanyOut]:
    """List all companies owned by the current user."""
    return get_companies_by_user(db, current_user.id)


@router.get("/{company_id}", response_model=CompanyOut)
def get_company_endpoint(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> CompanyOut:
    """Fetch a single company owned by the current user."""
    return get_company(db, company_id, current_user.id)


@router.put("/{company_id}", response_model=CompanyOut)
def update_company_endpoint(
    company_id: int,
    body: CompanyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> CompanyOut:
    """Update fields of a company owned by the current user."""
    return update_company(db, company_id, body, current_user.id)


@router.delete("/{company_id}", status_code=204)
def delete_company_endpoint(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> None:
    """Delete a company owned by the current user."""
    delete_company(db, company_id, current_user.id)