import http

from sqlalchemy.orm import Session
from .models import Post
from .schemas import PostCreate, PostUpdate
from fastapi.exceptions import HTTPException


def get_post_list(db: Session):
    return db.query(Post).all()


def creat_post(db: Session, item: PostCreate):
    post = Post(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_post_by_id(id: int, db: Session) -> Post:
    post = db.query(Post).get(id)

    if post is None:
        raise HTTPException(
            status_code=http.HTTPStatus.NOT_FOUND,
            detail=f"Post with id:{id} not found!"
        )

    return post


def update_post_by_id(id: int, data: PostUpdate, db: Session):
    post = db.query(Post).get(id)

    if post is None:
        raise HTTPException(
            status_code=http.HTTPStatus.NOT_FOUND,
            detail=f"Post with id:{id} not found!"
        )

    post.title = data.title
    post.text = data.text
    db.commit()
    db.refresh(post)
    return post


def delete_post_by_id(id: int, db: Session) -> bool:
    post = db.query(Post).get(id)

    if post is None:
        raise HTTPException(
            status_code=http.HTTPStatus.NOT_FOUND,
            detail=f"Post with id:{id} not found!"
        )

    db.delete(post)
    db.commit()

    return True
