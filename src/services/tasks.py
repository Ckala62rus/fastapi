from schemas.tasks.tasks_schema import (
    TaskSchemaAdd,
    TaskSchemaEdit,
    TaskSchemaDescriptionEdit,
)
from utils.unitofwork import IUnitOfWork


class TasksService:
    async def add_task(self, uow: IUnitOfWork, task: TaskSchemaAdd):
        tasks_dict = task.model_dump()
        async with uow:
            task_id = await uow.tasks.add_one(tasks_dict)
            model = await uow.tasks.find_one(id=task_id)
            await uow.commit()
            return model

    async def get_tasks(self, uow: IUnitOfWork):
        async with uow:
            tasks = await uow.tasks.find_all()
            return tasks

    async def get_task_by_id(self, uow: IUnitOfWork, task_id):
        async with uow:
            task = await uow.tasks.find_one(id=task_id)
            return task

    async def delete_task_by_id(self, uow: IUnitOfWork, task_id):
        async with uow:
            task = await uow.tasks.find_one(id=task_id)
            if task is not None:
                await uow.tasks.delete(task)
                await uow.commit()
                return task_id

            return None

    async def edit_task(self, uow: IUnitOfWork, task_id: int, task: TaskSchemaEdit):
        tasks_dict = task.model_dump()
        async with uow:
            await uow.tasks.edit_one(task_id, tasks_dict)

            curr_task = await uow.tasks.find_one(id=task_id)

            ##### edit or create some models within one transaction #####
            # task_history_log = TaskHistorySchemaAdd(
            #     task_id=task_id,
            #     previous_assignee_id=curr_task.assignee_id,
            #     new_assignee_id=task.assignee_id
            # )

            # task_history_log = task_history_log.model_dump()
            # await uow.task_history.add_one(task_history_log)

            await uow.commit()
            return curr_task

    async def update_task_description(
        self, uow: IUnitOfWork, task_id: int, task_data: TaskSchemaDescriptionEdit
    ):
        tasks_dict = task_data.model_dump()
        async with uow:
            await uow.tasks.edit_one(task_id, tasks_dict)
            curr_task = await uow.tasks.find_one(id=task_id)
            await uow.commit()
            return curr_task
