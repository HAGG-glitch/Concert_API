from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from crud import DirectorPlayServices

directorplay_router = APIRouter(prefix="/directorplay", tags= ["DirectorPlay"])

@directorplay_router.post("/", response_model= schemas.DirectorPlay)
async def create_directorplay(directorplay: schemas.CreateDirectorPlay,
                       db: Session = Depends(get_db)):
    return DirectorPlayServices.create_director_play(db, directorplay)

@directorplay_router.get("/", response_model=List[schemas.DirectorPlay])
def get_all_director_plays(db: Session = Depends(get_db)):
    return DirectorPlayServices.get_all_director_plays(db)

@directorplay_router.get("/{directorplay_id}", response_model=schemas.DirectorPlay)
def get_director_play(directorplay_id: int, db: Session = Depends(get_db)):
    return DirectorPlayServices.get_director_play(db, directorplay_id)

@directorplay_router.delete("/{directorplay_id}")
def delete_director_play(directorplay_id: int, db: Session = Depends(get_db)):
    DirectorPlayServices.delete_director_play(db, directorplay_id)
    return {"message": "Deleted successfully"}