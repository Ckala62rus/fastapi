from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.utils import get_db
from domain import service
from domain.schemas import PostCreate, PostList
from user.auth_jwt_middleware import JWTBearer


router = APIRouter(tags=["Posts"])


@router.get("", response_model=List[PostList], dependencies=[Depends(JWTBearer())])
def post_list(db: Session = Depends(get_db)):
    return service.get_post_list(db)


@router.post("")
def post_list(item: PostCreate, db: Session = Depends(get_db)):
    return service.creat_post(db, item)
