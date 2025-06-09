from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from services import SeatServices

seat_router = APIRouter(prefix="/seat", tags= ["Seat"])

@seat_router.post("/", response_model= schemas.Seat)
async def create_seat(seat: schemas.CreateSeat,
                       db: Session = Depends(get_db)):
    return SeatServices.create_seat(db, seat)