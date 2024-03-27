from fastapi import APIRouter, Depends
from typing import Annotated, List

from schemas.tasks.tasks_schema import TaskSchemaAdd, TaskSchema
from services.tasks import TasksService
from utils.dependencies import UOWDep

route = APIRouter(tags=["Tasks"])


@route.get(
    "/",
    description="Get all tasks",
    response_model=List[TaskSchema]
)
async def get_tasks(uow: UOWDep):
    tasks = await TasksService().get_tasks(uow)
    return tasks


@route.post(
    "/",
    description="Get all tasks",
    response_model=TaskSchema
)
async def create_task(task: Annotated[TaskSchemaAdd, Depends()], uow: UOWDep):
    return await TasksService().add_task(uow, task)
