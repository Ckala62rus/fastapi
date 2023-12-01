from fastapi import APIRouter

from domain.handler import router as post_routers


routes = APIRouter()

routes.include_router(post_routers, prefix="/posts")
