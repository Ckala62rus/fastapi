from utils.repository import SQLAlchemyRepository
from models.task import Task


class TasksRepository(SQLAlchemyRepository):
     model = Task
