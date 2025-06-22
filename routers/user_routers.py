from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

import schemas
from database import get_db
from schemas import UserCreate, UserOut
from crud import user_services
from security.security_roles import require_role, get_current_user

user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return user_services.create_user(db, user)

@user_router.get("/count")
def user_count(
    db: Session = Depends(get_db),
    current_user: schemas.Customer = Depends(require_role("admin"))  # Admin only
):
    return {"total_users": user_services.count_users(db)}

@user_router.get("/", response_model=List[UserOut])
def get_all_users(
    db: Session = Depends(get_db),
    get_current_user: schemas.Customer = Depends(require_role("admin"))  # Admin only
):
    return user_services.get_all_users(db)

@user_router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    get_current_user: schemas.Customer = Depends(require_role("admin"))  # Admin only
):
    return user_services.get_user_by_id(db, user_id)
