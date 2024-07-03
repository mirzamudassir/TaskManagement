# project.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from .database import SessionLocal
from . import schemas
from .models import Project, User

router = APIRouter()

# Dependency: get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/v1/project", response_model=schemas.ProjectListResponse)
def list_assigned_projects(db: Session = Depends(get_db)):
    # Example assuming authentication and fetching user's assigned projects
    # Replace with your actual logic based on your application's authentication and authorization
    # For demonstration purposes, let's assume we fetch projects for a specific user
    user_id = 1  # Replace with actual authenticated user id or retrieve from JWT token

    # Fetch user from database
    user = db.query(User).filter(User.id == user_id).first()

    if user:
        # Access projects assigned to the user
        assigned_projects = user.projects
        return {"projects": [{"id": project.id, "name": project.name} for project in assigned_projects]}
    else:
        return {"projects": []}  # Return an empty list if user not found or has no projects
