from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from services import PlayServices

play_router = APIRouter(prefix="/play", tags= ["Play"])

@play_router.post("/", response_model= schemas.Play)
async def create_play(play: schemas.PlayCreate,
                       db: Session = Depends(get_db)):
    return PlayServices.create_play(db, play)