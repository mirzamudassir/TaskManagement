# user.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from .database import SessionLocal
from . import schemas
from .models import User as DBUser

router = APIRouter()

# Dependency: get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/v1/admin/user", response_model=List[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    users = db.query(DBUser).all()
    return users
