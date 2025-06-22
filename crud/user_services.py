from typing import Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import User
from schemas import UserCreate
from security.security import get_password_hash


def create_user(db: Session, user: UserCreate) -> User:
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")

    hashed_pw = get_password_hash(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def count_users(db: Session) -> int:
    return db.query(User).count()

def get_all_users(db: Session) -> list[type[User]]:
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()
