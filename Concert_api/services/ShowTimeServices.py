from sqlalchemy.orm import Session

import schemas
from typing import Optional, List
from models import ShowTime
from datetime import date


def create_showtime(db: Session, showtime_data: schemas.CreateShowTime):
    showtime = ShowTime(
        date_time = showtime_data.date_time,
        play_id = showtime_data.play_id
    )

    db.add(showtime)
    db.commit()
    db.refresh(showtime)
    return showtime
