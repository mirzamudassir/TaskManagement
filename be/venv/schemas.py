from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import enum

class RoleEnum(str, enum.Enum):
    admin = "admin"
    user = "user"

class UserBase(BaseModel):
    name: str
    email: str
    role: RoleEnum = RoleEnum.user

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    name: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str

class TaskCreate(TaskBase):
    project_id: int
    assignee_id: int

class Task(TaskBase):
    id: int
    parent_id: Optional[int] = None
    project_id: int
    assignee_id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    task_id: int

class Comment(CommentBase):
    id: int
    parent_id: Optional[int] = None
    task_id: int
    timestamp: datetime

    class Config:
        orm_mode = True
