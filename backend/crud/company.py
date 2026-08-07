

from backend.model.company import Company


def create_company(db: Session, company: CompanyCreate):
    db_company = Company(name=company.name, description=company.description)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company