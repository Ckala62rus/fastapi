pip install sqlalchemy
pip install psycopg2-binary
pip install alembic
pip install pipenv
pipenv shell
pipenv install fastapi[all]

##### database fastapi

alembic init migrations
alembic revision --autogenerate -m "init"
alembic upgrade head
