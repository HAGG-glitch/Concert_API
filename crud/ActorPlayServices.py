from sqlalchemy.orm import  Session
from fastapi import  HTTPException
import schemas
from typing import  Optional, List
from models import ActorPlay
from datetime import date

def create_actor_play(db: Session, actorplay_data: schemas.CreateActorPlay):
    actorplay = ActorPlay(
        actor_id =  actorplay_data.actor_id,
        play_id = actorplay_data.play_id
    )

    db.add(actorplay)
    db.commit()
    db.refresh(actorplay)
    return actorplay

def get_all_actor_plays(db: Session) -> List[type[ActorPlay]]:
    return db.query(ActorPlay).all()

def get_actor_play(db: Session, actorplay_id: int) -> Optional[ActorPlay]:
    record = db.query(ActorPlay).filter(ActorPlay.id == actorplay_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="ActorPlay not found")
    return record

def delete_actor_play(db: Session, actorplay_id: int):
    record = db.query(ActorPlay).filter(ActorPlay.id == actorplay_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="ActorPlay not found")
    db.delete(record)
    db.commit()
