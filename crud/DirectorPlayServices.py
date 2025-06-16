from sqlalchemy.orm import Session
from fastapi import HTTPException
import schemas
from typing import Optional, List
from models import DirectorPlay
from datetime import date


def create_director_play(db: Session, directorplay_data: schemas.CreateDirectorPlay):
    director_play = DirectorPlay(
        director_id = directorplay_data.director_id,
        play_id = directorplay_data.play_id
    )

    db.add(director_play)
    db.commit()
    db.refresh(director_play)
    return director_play


def get_all_director_plays(db: Session) -> List[type(DirectorPlay)]:
    return db.query(DirectorPlay).all()

def get_director_play(db: Session, directorplay_id: int) -> Optional[DirectorPlay]:
    record = db.query(DirectorPlay).filter(DirectorPlay.id == directorplay_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="DirectorPlay not found")
    return record


def delete_director_play(db: Session, directorplay_id: int):
    record = db.query(DirectorPlay).filter(DirectorPlay.id == directorplay_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="DirectorPlay not found")
    db.delete(record)
    db.commit()