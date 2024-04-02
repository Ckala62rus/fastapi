from pathlib import Path

from starlette.requests import Request

BASE_DIR = Path(__file__).parent.parent


def get_db(request: Request):
    return request.state.db
