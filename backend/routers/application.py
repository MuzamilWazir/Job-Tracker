from fastapi import APIRouter , Depends

from crud.application import create_application, delete_application, get_application, get_applications_by_user, update_application, update_application_status
from dependencies import get_current_user, get_db
from models.user import User
from schemas.application import ApplicationCreate, ApplicationOut , ApplicationUpdate , ApplicationStatusUpdate
from typing import Optional
from sqlalchemy.orm import Session

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/" , response_model = ApplicationOut)
def create_application_endpoint(body : ApplicationCreate , db : Session = Depends(get_db), current_user: User = Depends(get_current_user)  ):
 return create_application(db , body , current_user.id)

@router.get("/" , response_model = list[ApplicationOut])
def get_applications_endpoint(db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_applications_by_user(db, current_user.id)


@router.get("/{application_id}" , response_model = ApplicationOut)
def get_application_endpoint(application_id : int , db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_application(db , application_id , current_user.id)   

@router.put("/{application_id}" , response_model = ApplicationOut)
def update_application_endpoint(application_id : int , body : ApplicationUpdate , db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_application(db , application_id , body , current_user.id)


@router.patch("/{application_id}/status" , response_model = ApplicationOut)
def update_application_status_endpoint(application_id : int , body : ApplicationStatusUpdate , db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_application_status(db , application_id , body , current_user.id)

@router.delete("/{application_id}" , status_code = 204)
def delete_application_endpoint(application_id : int , db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return delete_application(db , application_id , current_user.id)


