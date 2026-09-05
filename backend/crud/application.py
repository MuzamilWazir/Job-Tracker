
from sqlalchemy.orm import Session
from models.application import Application
from schemas.application import ApplicationCreate, ApplicationUpdate



def create_application(db : Session, data : ApplicationCreate, user_id : int):
    new_application =  Application(
    job_title = data.job_title,
    notes = data.notes,
    company = data.company_id,
    user_id = user_id
    )

    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return new_application

def get_applications_by_user(db : Session, user_id : int, status=None):
    query = db.query(Application).filter(Application.user_id == user_id)
    if status:
        query = query.filter(Application.status == status)
    return query.all()

