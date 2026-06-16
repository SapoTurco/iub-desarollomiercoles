from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from config.database import get_db
from schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate
from services.task_service import TaskService
from utils.dependencies import get_current_user
from model.user_model import User

router = APIRouter(
    prefix='/tasks',
    tags=['tasks'],
)

@router.post('/', response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TaskService(db=db)
    return service.create_task(task_data, current_user)


@router.get('/', response_model=list[TaskResponse])
def list_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TaskService(db=db)
    return service.list_tasks(current_user)


@router.get('/{task_id}', response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TaskService(db=db)
    return service.get_task(task_id, current_user)


@router.put('/{task_id}', response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TaskService(db=db)
    return service.update_task(task_id, task_data, current_user)


@router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TaskService(db=db)
    service.delete_task(task_id, current_user)
