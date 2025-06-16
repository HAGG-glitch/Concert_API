from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import ShowTime
import schemas
from typing import List
def create_showtime(db: Session, showtime_data: schemas.CreateShowTime) -> ShowTime:
    showtime = ShowTime(
        play_id=showtime_data.play_id,
        date=showtime_data.date
    )
    db.add(showtime)
    db.commit()
    db.refresh(showtime)
    return showtime

def get_all_showtime(db: Session) -> List[type[ShowTime]]:
    return db.query(ShowTime).all()

def get_showtime_by_id(db: Session, showtime_id: int) -> ShowTime:
    showtime = db.query(ShowTime).filter(ShowTime.id == showtime_id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return showtime


def update_showtime(db: Session, showtime_id: int, showtime_update: schemas.UpdateShowTime) -> ShowTime:
    showtime = db.query(ShowTime).filter(ShowTime.id == showtime_id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")

    update_data = showtime_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(showtime, key, value)

    db.commit()
    db.refresh(showtime)
    return showtime

def partial_update_showtime(db:Session, showtime_id: int,showtime_data: schemas.UpdateShowTime ) -> ShowTime:
    showtime = db.query(ShowTime).filter(ShowTime.id == showtime_id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    if showtime_data.date is not None:
        showtime.date = showtime_data.date
    if showtime_data.play_id is not None:
        showtime.play_id = showtime_data.play_id
    db.commit()
    db.refresh(showtime)
    return showtime

def delete_showtime(db: Session, showtime_id: int):
    showtime = db.query(ShowTime).filter(ShowTime.id == showtime_id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    db.delete(showtime)
    db.commit()


