from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class TaskPriority(str, Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'


class TaskStatus(str, Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    completed = 'completed'


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: TaskPriority = TaskPriority.low
    status: TaskStatus = TaskStatus.pending


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[TaskPriority] = None
    status: Optional[TaskStatus] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: TaskPriority
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    model_config = {'from_attributes': True}
