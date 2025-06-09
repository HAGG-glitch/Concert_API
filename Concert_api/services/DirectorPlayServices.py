from sqlalchemy.orm import Session

import schemas
from typing import Optional, List
from models import DirectorPlay
from datetime import date


def create_director_play(db: Session, directorplay_data: schemas.DirectorPlay):
    director_play = DirectorPlay(
        director_id = directorplay_data.director_id,
        play_id = directorplay_data.play_id
    )

    db.add(director_play)
    db.commit()
    db.refresh(director_play)
    return director_play
