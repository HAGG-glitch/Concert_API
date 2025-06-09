from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from services import ActorServices

actor_router = APIRouter(prefix="/actor", tags= ["Actor"])

@actor_router.post("/", response_model= schemas.Actor)
async def create_actor(actor: schemas.CreateActor,
                       db: Session = Depends(get_db)):
    return ActorServices.create_actor(db, actor)