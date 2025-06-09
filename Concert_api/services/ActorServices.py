from sqlalchemy.orm import Session
import schemas
from typing import Optional, List
from models import Actor
from datetime import date


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
