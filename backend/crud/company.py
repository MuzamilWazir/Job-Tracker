from schemas.company import CompanyCreate
from models.company import Company

def create_company(company: CompanyCreate, db):
    new_company = Company(**company.model_dump())
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return {
        "message": "Company created successfully!",
        "company": new_company
    }