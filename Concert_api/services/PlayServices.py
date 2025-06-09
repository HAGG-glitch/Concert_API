from sqlalchemy.orm import Session

import schemas
from typing import Optional, List
from models import Play
from datetime import date


def create_play(db: Session, play_data: schemas.PlayCreate):
    play = Play(
        title = play_data.title,
        duration = play_data.duration,
        genre = play_data.genre,
        synopsis = play_data.synopsis,
    )

    db.add(play)
    db.commit()
    db.refresh(play)
    return play
