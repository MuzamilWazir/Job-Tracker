from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.company import Company
from schemas.company import CompanyCreate, CompanyUpdate


def create_company(db: Session, data: CompanyCreate, user_id: int) -> Company:
    new_company = Company(
        name=data.name,
        website=data.website,
        notes=data.notes,
        user_id=user_id
    )
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company


def get_companies_by_user(db: Session, user_id: int) -> list[Company]:
    return db.query(Company).filter(Company.user_id == user_id).all()


def get_company(db: Session, company_id: int, user_id: int) -> Company:
    company = db.query(Company).filter(
        Company.id == company_id, Company.user_id == user_id
    ).first()
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return company


def update_company(db: Session, company_id: int, data: CompanyUpdate, user_id: int) -> Company:
    company = get_company(db, company_id, user_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(company, key, value)
    db.commit()
    db.refresh(company)
    return company


def delete_company(db: Session, company_id: int, user_id: int) -> None:
    company = get_company(db, company_id, user_id)
    db.delete(company)
    db.commit()