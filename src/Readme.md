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
pip install -U "celery[redis]"
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
alembic history
alembic downgrade 8ac14e223d1e
```

### run application
uvicorn main:app --reload

### celery start
```Bash
celery -A tasks.tasks.celery worker --loglevel=INFO --pool=solo
```
> --pool=solo fow run windows

### celery flower start
```Bash
celery -A tasks.tasks.celery flower --port=5555
celery --broker=redis://localhost:6379/0 flower --port=5555
```
