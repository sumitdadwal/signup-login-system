from fastapi import APIRouter, Depends
from routers.schemas import UserDisplay, UserBase
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.db_user import new_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return new_user(db, request)