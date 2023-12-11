import time

import requests
from fastapi import Depends, APIRouter, Request
from sqlalchemy.orm import Session

from core.utils import get_db
from user.auth_handler import sign_jwt, check_user, decode_jwt
from user.auth_jwt_middleware import JWTBearer
from user.user import User, UserLoginSchema, UserMe
from user.user_service import make_hash_password, get_user, parse_authorization_header
from tasks.tasks import telegram

router = APIRouter(tags=["Users"])


@router.post(
    "/signup",
    response_model=dict,
    description="Registration user",
    name="Registration user (SignIn)"
)
async def create_user(user: UserLoginSchema, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    new_user.password = make_hash_password(new_user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return sign_jwt(new_user.email)


@router.post("/login")
async def user_login(user: UserLoginSchema, db: Session = Depends(get_db)):
    if check_user(user, db):
        response = sign_jwt(user.email)
        return response
    return {
        "error": "Wrong login details!"
    }


@router.get(
    "/me",
    dependencies=[Depends(JWTBearer())],
    response_model=UserMe,
    description="Get authenticated current user model",
    name="Get current user"
)
# async def me(email: str, db: Session = Depends(get_db)):
async def me(request: Request, db: Session = Depends(get_db)):
    token = parse_authorization_header(request)
    result = decode_jwt(token)
    return get_user(result["email"], db)


@router.get(
    "send-message",
    description="Send test message to telegram",
    name="Send message to telegram"
)
async def send_message(message: str) -> dict:
    # url = "https://api.telegram.org/bot5853484688:AAFzfJEjnHv3AMgWCpO5bsj6UhqgusvnkZc/sendMessage"
    # response = requests.get(
    #     url,
    #     params={
    #         "chat_id": 803431360,
    #         "text": message
    #     }
    # )
    # res = response.json()
    telegram.delay(message)
    return {
        "success": True,
        "message": message,
        # "res": res
    }
