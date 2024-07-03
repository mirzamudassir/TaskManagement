from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import enum

class RoleEnum(enum.Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    role = Column(Enum(RoleEnum), default=RoleEnum.user)

    projects = relationship("Project", secondary="user_project", back_populates="users")
    tasks = relationship("Task", back_populates="assignee")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    users = relationship("User", secondary="user_project", back_populates="projects")
    tasks = relationship("Task", back_populates="project")

class UserProject(Base):
    __tablename__ = "user_project"

    project_id = Column(Integer, ForeignKey("projects.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("tasks.id"), nullable=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    title = Column(String, index=True)
    description = Column(Text)
    status = Column(String, index=True)
    assignee_id = Column(Integer, ForeignKey("users.id"))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    project = relationship("Project", back_populates="tasks")
    assignee = relationship("User", back_populates="tasks")
    comments = relationship("Comment", back_populates="task")
    subtasks = relationship("Task", back_populates="parent", remote_side=[id])

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("comments.id"), nullable=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    content = Column(Text)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    task = relationship("Task", back_populates="comments")
    replies = relationship("Comment", back_populates="parent", remote_side=[id])
    parent = relationship("Comment", back_populates="replies")
