from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from services import ActorPlayServices

actorplay_router = APIRouter(prefix="/actorplay", tags= ["ActorPlays"])

@actorplay_router.post("/", response_model= schemas.ActorPlay)
async def create_actorplay(actorplay: schemas.ActorPlay,
                       db: Session = Depends(get_db)):
    return ActorPlayServices.create_actor_play(db, actorplay)