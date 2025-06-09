from sqlalchemy.orm import Session

import schemas
from typing import Optional, List
from models import Price
from datetime import date


def create_price(db: Session, price_data: schemas.CreatePrice):
    price = Price(
        seat_row_no= price_data.seat_row_no,
        seat_seat_no = price_data.seat_seat_no,
        showtime_date_time = price_data.showtime_date_time,
        showtime_play_id = price_data.showtime_play_id,
        price = price_data.price
    )

    db.add(price)
    db.commit()
    db.refresh(price)
    return price
