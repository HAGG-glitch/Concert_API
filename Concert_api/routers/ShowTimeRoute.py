from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from services import ShowTimeServices

showtime_router = APIRouter(prefix="/showtime", tags= ["ShowTime"])

@showtime_router.post("/", response_model= schemas.ShowTime)
async def create_showtime(showtime: schemas.CreateShowTime,
                       db: Session = Depends(get_db)):
    return ShowTimeServices.create_showtime(db, showtime)