from fastapi import APIRouter, Response
from typing import List

from starlette import status

from schemas.tasks.tasks_schema import TaskSchemaAdd, TaskSchema, TaskSchemaEdit
from services.tasks import TasksService
from utils.dependencies import UOWDep

route = APIRouter(tags=["Tasks"])


@route.get("/", description="Get all tasks", response_model=List[TaskSchema])
async def get_tasks(uow: UOWDep):
    tasks = await TasksService().get_tasks(uow)
    return list(tasks)


@route.post(
    "/",
    description="Get all tasks",
    status_code=status.HTTP_201_CREATED,
    response_model=TaskSchema,
)
async def create_task(task: TaskSchemaAdd, uow: UOWDep):
    return await TasksService().add_task(uow, task)


@route.get("/{task_id}", status_code=status.HTTP_200_OK)
async def get_task_by_id(task_id: int, uow: UOWDep, response: Response):
    task = await TasksService().get_task_by_id(uow, task_id=task_id)

    if task is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"task with id:{task_id} not found."}

    return task


@route.put("/{task_id}", status_code=status.HTTP_200_OK)
async def update_task_by_id(
    task_id: int, task_for_update: TaskSchemaEdit, uow: UOWDep, response: Response
):
    task = await TasksService().edit_task(
        uow=uow, task_id=task_id, task=task_for_update
    )

    if task is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"task with id:{task_id} not found."}

    return task


@route.delete("/{task_id}/", status_code=status.HTTP_200_OK)
async def delete_task_by_id(task_id: int, uow: UOWDep, response: Response):
    task = await TasksService().delete_task_by_id(uow=uow, task_id=task_id)

    if task is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"can not delete. task with id:{task_id} not found."}

    return task
