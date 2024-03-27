from fastapi import APIRouter

from domain.handler import router as post_routers
from user.handler import router as user_routes
from api.tasks import route as tasks_routes


routes = APIRouter()

routes.include_router(post_routers, prefix="/posts")
routes.include_router(user_routes, prefix="/users")
routes.include_router(tasks_routes, prefix="/tasks")
