## Dependencies

```Bash
pip install sqlalchemy
pip install psycopg2-binary
pip install alembic
pip install pipenv
pip install pyJWT
pip install python-decouple
pip install pydantic[email]
pipenv shell
pipenv install fastapi[all]
```

### Install all dependencies
```Bash
pip install -r requirements.txt
```
### Database fastapi

```Bash
alembic init migrations
alembic revision --autogenerate -m "init"
alembic upgrade head
```

### run application
uvicorn main:app --reload
