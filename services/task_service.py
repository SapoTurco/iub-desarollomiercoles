from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from model.task_model import Task
from repositories.task_repository import TaskRepository
from schemas.task_schema import TaskCreate, TaskUpdate
from model.user_model import User


class TaskService:
    def __init__(self, db: Session):
        self.task_repository = TaskRepository(db=db)

    def create_task(self, task_data: TaskCreate, owner: User) -> Task:
        task = Task(
            title=task_data.title,
            description=task_data.description,
            priority=task_data.priority.value,
            status=task_data.status.value,
            owner_id=owner.id,
        )
        return self.task_repository.create(task)

    def list_tasks(self, owner: User) -> list[Task]:
        return self.task_repository.list_by_owner(owner.id)

    def get_task(self, task_id: int, owner: User) -> Task:
        task = self.task_repository.get_by_id_and_owner(task_id, owner.id)
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Tarea no encontrada',
            )
        return task

    def update_task(self, task_id: int, task_data: TaskUpdate, owner: User) -> Task:
        task = self.get_task(task_id, owner)
        update_data = task_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(task, field, value.value if hasattr(value, 'value') else value)
        return self.task_repository.update(task)

    def delete_task(self, task_id: int, owner: User) -> None:
        task = self.get_task(task_id, owner)
        self.task_repository.delete(task)
