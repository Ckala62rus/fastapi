from fastapi import FastAPI

from core.db import SessionLocal
from routes import routes
from starlette.responses import Response
from starlette.requests import Request


app = FastAPI(
    title="Fastapi example",
    description="Example REST api on FastApi",
    version="1.0",
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(routes)
