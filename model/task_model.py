from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[String] = mapped_column(String(255), nullable=False)
    description: Mapped[String] = mapped_column(String(1000), nullable=True)
    priority: Mapped[String] = mapped_column(String(50), nullable=False, default='low')
    status: Mapped[String] = mapped_column(String(50), nullable=False, default='pending')
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    owner = relationship('User', back_populates='tasks')
