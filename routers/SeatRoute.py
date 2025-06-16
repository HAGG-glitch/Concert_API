from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas
from crud import SeatServices
from database import get_db

seat_router = APIRouter(prefix="/seat", tags=["Seat"])

@seat_router.post("/", response_model=schemas.Seat)
async def create_seat(seat: schemas.CreateSeat, db: Session = Depends(get_db)):
    return SeatServices.create_seat(db, seat)

@seat_router.get("/", response_model=list[schemas.Seat])
def get_all_seats(db: Session = Depends(get_db)):
    return SeatServices.get_all_seats(db)

@seat_router.get("/{seat_id}", response_model=schemas.Seat)
def get_seat(seat_id: int, db: Session = Depends(get_db)):
    return SeatServices.get_seat_by_id(db, seat_id)

@seat_router.put("/{seat_id}", response_model=schemas.Seat)
async def update_seat(seat_id: int, seat_data: schemas.UpdateSeat, db: Session = Depends(get_db)):
    return SeatServices.update_seat(db, seat_id, seat_data)

@seat_router.patch("/{seat_id}", response_model=schemas.Seat)
async def partial_update_seat(seat_id: int, seat_data: schemas.UpdateSeat, db: Session = Depends(get_db)):
    return SeatServices.update_seat(db,seat_id, seat_data)

@seat_router.delete("/{seat_id}")
def delete_seat(seat_id: int, db: Session = Depends(get_db)):
    return SeatServices.delete_seat(db, seat_id)
