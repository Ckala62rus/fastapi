import http

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.utils import get_db
from domain import service
from domain.schemas import PostCreate, PostList, PostUpdate
from user.auth_jwt_middleware import JWTBearer


router = APIRouter(tags=["Posts"])


@router.get(
    "",
    # response_model=List[PostList],
    # response_model=dict,
    dependencies=[Depends(JWTBearer())],
    status_code=http.HTTPStatus.OK
)
def post_list(db: Session = Depends(get_db)):
    try:
        data = service.get_post_list(db)
        return {
            "status": True,
            "data": data,
            "message": None,
        }
    except Exception as ex:
        return {
            "status": True,
            "data": None,
            "message": ex,
        }


@router.post(
    "",
    response_model=PostList,
    dependencies=[Depends(JWTBearer())],
    status_code=http.HTTPStatus.CREATED
)
def post_list(item: PostCreate, db: Session = Depends(get_db)):
    data = service.creat_post(db, item)
    return {
        "status": True,
        "data": data,
        "message": None,
    }


@router.get(
    "/{id}",
    status_code=http.HTTPStatus.OK,
    dependencies=[Depends(JWTBearer())],
    description="Get post by id",
)
def post_by_id(id: int, db: Session = Depends(get_db)):
    try:
        post = service.get_post_by_id(id, db)
        return {
            "status": True,
            "data": post,
            "message": None,
        }
    except Exception as ex:
        return {
            "status": False,
            "data": None,
            "message": ex,
        }


@router.put(
    "/{id}",
    name="Update post",
    description="Update post by id",
    status_code=http.HTTPStatus.OK,
    dependencies=[Depends(JWTBearer())],
)
def post_update_by_id(id: int, data: PostUpdate, db: Session = Depends(get_db)):
    try:
        post = service.update_post_by_id(id, data, db)
        return {
            "status": True,
            "data": post,
            "message": None,
        }
    except Exception as ex:
        return {
            "status": False,
            "data": None,
            "message": ex,
        }


@router.delete(
    "/{id}",
    status_code=http.HTTPStatus.OK,
    name="Delete post by id",
    description="Delete post",
    dependencies=[Depends(JWTBearer())],
)
def post_delete_by_id(id: int, db: Session = Depends(get_db)):
    try:
        service.delete_post_by_id(id, db)
        return {
            "status": True,
            "data": None,
            "message": f"Post with id:{id} was deleted",
        }
    except Exception as ex:
        return {
            "status": False,
            "data": None,
            "message": ex,
        }
