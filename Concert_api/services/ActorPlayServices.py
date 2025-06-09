from sqlalchemy.orm import  Session

import schemas
from typing import  Optional, List
from models import ActorPlay
from datetime import date

def create_actor_play(db: Session, actorplay_data: schemas.ActorPlay):
    actorplay = ActorPlay(
        actor_id =  actorplay_data.actor_id,
        play_id = actorplay_data.play_id

    )

    db.add(actorplay)
    db.commit()
    db.refresh(actorplay)
    return actorplay
