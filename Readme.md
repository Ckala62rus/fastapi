## Dependencies

> - pip install sqlalchemy
> - pip install psycopg2-binary
> - pip install alembic
> - pip install pipenv
> - pipenv shell
> - pipenv install fastapi[all]

### Install all dependencies
>   pip install -r requirements.txt

### Database fastapi

> - alembic init migrations
> - alembic revision --autogenerate -m "init"
> - alembic upgrade head


### run application
uvicorn main:app --reload
