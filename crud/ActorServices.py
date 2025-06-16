from sqlalchemy.orm import Session
import schemas
from typing import Optional, List
from models import Actor
from datetime import date
from fastapi import HTTPException

def create_actor(db: Session, actor_data: schemas.CreateActor):
    actor = Actor(
        name = actor_data.name,
        gender = actor_data.gender,
        dob = actor_data.dob,

    )

    db.add(actor)
    db.commit()
    db.refresh(actor)
    return actor

def get_all_actors(db: Session) -> List[type[Actor]]:
    return db.query(Actor).all()

def get_actor(db: Session, actor_id: int) -> Optional[Actor]:
    return db.query(Actor).filter(Actor.id == actor_id).first()

def update_actor(db: Session, actor_id: int, actor_data: schemas.UpdateActor) -> Actor:
    actor = db.query(Actor).filter(Actor.id == actor_id).first()
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    actor.name = actor_data.name
    actor.gender = actor_data.gender
    actor.dob = actor_data.dob
    db.commit()
    db.refresh(actor)
    return actor

def partial_update_actor(db: Session, actor_id: int, actor_data: schemas.UpdateActor) -> Actor:
    actor = db.query(Actor).filter(Actor.id == actor_id).first()
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    if actor_data.name is not None:
        actor.name = actor_data.name
    if actor_data.gender is not None:
        actor.gender = actor_data.gender
    if actor_data.dob is not None:
        actor.dob = actor_data.dob
    db.commit()
    db.refresh(actor)
    return actor

def delete_actor(db: Session, actor_id: int):
    actor = db.query(Actor).filter(Actor.id == actor_id).first()
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    db.delete(actor)
    db.commit()