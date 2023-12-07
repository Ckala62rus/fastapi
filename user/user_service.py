from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import Session
from fastapi import Request

from user.user import User, UserMe


def make_hash_password(password: str) -> str:
    """
    Convert string to hash.
    Example:
        input: toomanysecrets
        output: $pbkdf2-sha256$29000$N2YMIWQsBWBMae09x1jrPQ$1t8iyB2A.WF/Z5JZv.lfCIhXXN33N23OSgQYThBYRfk

    :param password:
    :return: hash
    """
    return pbkdf2_sha256.hash(password)


def compare_hash_password(input_password: str, password_form_database: str) -> bool:
    """
    Compare input user password(hash) with passwordstore in database,
    and return True or False

    :param input_password:
    :param password_form_database:
    :return:
    """
    return pbkdf2_sha256.verify(input_password, password_form_database)


def get_user(email: str, db: Session) -> UserMe:
    user = db.query(User).filter(User.email == email).first()
    return UserMe(id=user.id, email=user.email)


def parse_authorization_header(request: Request) -> str:
    """
    Parse authorization header from request. And return
    token
    :param request: Request from Fastapi package
    :return: Token from authentication header request
    """
    header = request.headers.get('Authorization')
    if header is None:
        raise "Header Authorization is None"
    return header.split(" ")[1]
