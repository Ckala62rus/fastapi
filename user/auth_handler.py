import time
from typing import Dict

import jwt
from sqlalchemy.orm import Session

from core import db
from user.user import UserLoginSchema, User

JWT_SECRET = "veryVerySecretKey"
JWT_ALGORITHM = "HS256"


def token_response(token: str):
    return {
        "access_token": token
    }


def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}


def check_user(data: UserLoginSchema, db: Session):
    users = db.query(User).all()
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False