from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from crud import ShowTimeServices

showtime_router = APIRouter(prefix="/showtime", tags= ["ShowTime"])

@showtime_router.post("/", response_model= schemas.ShowTime)
async def create_showtime(showtime: schemas.CreateShowTime,
                       db: Session = Depends(get_db)):
    return ShowTimeServices.create_showtime(db, showtime)

@showtime_router.get("/", response_model=list[schemas.ShowTime])
def get_all_showtimes(db: Session = Depends(get_db)):
    return ShowTimeServices.get_all_showtime(db)

@showtime_router.get("/{showtime_id}", response_model=schemas.ShowTime)
def get_showtime(showtime_id: int, db: Session = Depends(get_db)):
    db_showtime = ShowTimeServices.get_showtime_by_id(db, showtime_id)
    if not db_showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return db_showtime

@showtime_router.put("/{showtime_id}", response_model=schemas.ShowTime)
async def update_showtime(showtime_id: int, showtime_data: schemas.UpdateShowTime, db: Session = Depends(get_db)):
    return ShowTimeServices.update_showtime(db, showtime_id, showtime_data)

@showtime_router.patch("/{showtime_id}", response_model=schemas.ShowTime)
async def partial_update_showtime(showtime_id: int, showtime_data: schemas.UpdateShowTime, db: Session = Depends(get_db)):
    return ShowTimeServices.partial_update_showtime(db,showtime_id, showtime_data)


@showtime_router.delete("/{showtime_id}")
def remove_showtime(showtime_id: int, db: Session = Depends(get_db)):
    return ShowTimeServices.delete_showtime(db, showtime_id)