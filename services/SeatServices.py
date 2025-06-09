from sqlalchemy.orm import Session

import schemas
from typing import Optional, List
from models import Seat
from datetime import date


def create_seat(db: Session, seat_data: schemas.CreateSeat):
    seat = Seat(
        row_no = seat_data.row_no,
        seat_no = seat_data.seat_no
    )

    db.add(seat)
    db.commit()
    db.refresh(seat)
    return seat
