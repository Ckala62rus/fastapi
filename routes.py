from fastapi import APIRouter

from domain.handler import router as post_routers
from user.handler import router as user_routes


routes = APIRouter()

routes.include_router(post_routers, prefix="/posts")
routes.include_router(user_routes, prefix="/users")
