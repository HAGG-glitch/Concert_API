from sqlalchemy.orm import Session
from fastapi import HTTPException
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


def get_all_plays(db: Session) -> List[type[Play]]:
    return db.query(Play).all()

def get_play(db: Session, play_id: int) -> Optional[Play]:
    return db.query(Play).filter(Play.id == play_id).first()

def update_play(db: Session, play_id: int, play_data: schemas.PlayUpdate) -> Play:
    play = db.query(Play).filter(Play.id == play_id).first()
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    play.title = play_data.title
    play.duration = play_data.duration
    play.genre = play_data.genre
    play.synopsis = play_data.synopsis
    db.commit()
    db.refresh(play)
    return play

def partial_update_play(db: Session, play_id: int, play_data: schemas.PlayUpdate) -> Play:
    play = db.query(Play).filter(Play.id == play_id).first()
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    if play_data.title is not None:
        play.title = play_data.title
    if play_data.duration is not None:
        play.duration = play_data.duration
    if play_data.genre is not None:
        play.genre = play_data.genre
    if play_data.synopsis is not None:
        play.synopsis = play_data.synopsis
    db.commit()
    db.refresh(play)
    return play

def delete_play(db: Session, play_id: int):
    play = db.query(Play).filter(Play.id == play_id).first()
    if not play:
        raise HTTPException(status_code=404, detail="Actor not found")
    db.delete(play)
    db.commit()