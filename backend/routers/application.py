from fastapi import APIRouter , Depends

from backend.dependencies import get_current_user, get_db
from backend.models.user import User
from backend.schemas.application import ApplicationCreate, ApplicationOut





router =  APIRouter( prefix ="/application" ,  tags =["application"])



@router.post("/" , response_model = ApplicationOut)
def create_application(body : ApplicationCreate , db = Depends(get_db), current_user: User = Depends(get_current_user)  ):
 return create_application(db , body , current_user.id)
