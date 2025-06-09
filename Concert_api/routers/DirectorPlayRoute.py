from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from services import DirectorPlayServices

directorplay_router = APIRouter(prefix="/directorplay", tags= ["DirectorPlay"])

@directorplay_router.post("/", response_model= schemas.DirectorPlay)
async def create_directorplay(directorplay: schemas.DirectorPlay,
                       db: Session = Depends(get_db)):
    return DirectorPlayServices.create_director_play(db, directorplay)