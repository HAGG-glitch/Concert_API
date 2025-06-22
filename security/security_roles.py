from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Callable

from security.security import oauth2_scheme  # ensure this is exported from your main security module
from config import settings
from jose import JWTError, jwt
from database import get_db
from models import Customer, User  # assuming roles are in User model


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception
    return user


def require_role(*allowed_roles: str) -> Callable:
    """
    Dependency factory that ensures the current user has one of the allowed roles.
    Usage: `Depends(require_role("admin", "staff"))`
    """
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action"
            )
        return current_user
    return role_checker
