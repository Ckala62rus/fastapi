pip install sqlalchemy
pip install psycopg2-binary
pip install alembic

##### database fastapi

alembic init migrations
alembic revision --autogenerate -m "init"
alembic upgrade head
