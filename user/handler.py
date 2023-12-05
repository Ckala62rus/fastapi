from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from core.utils import get_db
from user.auth_handler import sign_jwt
from user.user import User, UserLoginSchema

router = APIRouter(tags=["Users"])


@router.post("/user/signup", response_model=dict)
async def create_user(user: UserLoginSchema, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return sign_jwt(new_user.email)
