from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

import schemas
from models import Seat


def create_seat(db: Session, seat_data: schemas.CreateSeat) -> Seat:
    seat = Seat(
                row_no=seat_data.row_no,
                seat_no=seat_data.seat_no
            )
    db.add(seat)
    db.commit()
    db.refresh(seat)
    return seat

def get_all_seats(db: Session) -> List[type[Seat]]:
    return db.query(Seat).all()

def get_seat_by_id(db: Session, seat_id: int) -> Seat:
    seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")
    return seat


def update_seat(db: Session, seat_id: int, seat_update: schemas.UpdateSeat) -> Seat:
    seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")

    update_data = seat_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(seat, key, value)

    db.commit()
    db.refresh(seat)
    return seat

def partial_update_seat(db:Session, seat_id: int,seat_data: schemas.UpdateSeat ) -> Seat:
    seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")
    if seat_data.row_no is not None:
        seat.row_no = seat_data.row_no
    if seat_data.seat_no is not None:
        seat.seat_no = seat_data.seat_no
    db.commit()
    db.refresh(seat)
    return seat

def delete_seat(db: Session, seat_id: int):
    seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")
    db.delete(seat)
    db.commit()
