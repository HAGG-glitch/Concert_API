from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session
from typing import List
from database import  get_db

import schemas

from crud import ActorPlayServices

actorplay_router = APIRouter(prefix="/actorplay", tags= ["ActorPlays"])

@actorplay_router.post("/", response_model= schemas.ActorPlay)
async def create_actorplay(actorplay: schemas.CreateActorPlay,
                       db: Session = Depends(get_db)):
    return ActorPlayServices.create_actor_play(db, actorplay)

@actorplay_router.get("/", response_model=List[schemas.ActorPlay])
def get_all_actor_plays(db: Session = Depends(get_db)):
    return ActorPlayServices.get_all_actor_plays(db)

@actorplay_router.get("/{actorplay_id}", response_model=schemas.ActorPlay)
def get_actor_play(actorplay_id: int, db: Session = Depends(get_db)):
    return ActorPlayServices.get_actor_play(db, actorplay_id)

@actorplay_router.delete("/{actorplay_id}")
def delete_actor_play(actorplay_id: int, db: Session = Depends(get_db)):
    ActorPlayServices.delete_actor_play(db, actorplay_id)
    return {"message": "Deleted successfully"}