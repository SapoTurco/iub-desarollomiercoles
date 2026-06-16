from sqlalchemy.orm import Session
from model.task_model import Task


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, task: Task) -> Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def list_by_owner(self, owner_id: int) -> list[Task]:
        return self.db.query(Task).filter(Task.owner_id == owner_id).all()

    def get_by_id_and_owner(self, task_id: int, owner_id: int) -> Task | None:
        return (
            self.db.query(Task)
            .filter(Task.id == task_id, Task.owner_id == owner_id)
            .first()
        )

    def delete(self, task: Task) -> None:
        self.db.delete(task)
        self.db.commit()

    def update(self, task: Task) -> Task:
        self.db.commit()
        self.db.refresh(task)
        return task
