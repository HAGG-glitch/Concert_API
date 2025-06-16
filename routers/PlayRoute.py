from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from crud import PlayServices

play_router = APIRouter(prefix="/play", tags= ["Play"])

@play_router.post("/", response_model= schemas.Play)
async def create_play(play: schemas.PlayCreate,
                       db: Session = Depends(get_db)):
    return PlayServices.create_play(db, play)

@play_router.get("/", response_model=list[schemas.Play])
async def get_all_plays(db: Session = Depends(get_db)):
    return PlayServices.get_all_plays(db)

@play_router.get("/{play_id}", response_model=schemas.Play)
async def get_play(play_id: int, db: Session = Depends(get_db)):
    play = PlayServices.get_play(db, play_id)
    if play is None:
        raise HTTPException(status_code=404, detail="Play not found")
    return play

@play_router.put("/{play_id}", response_model=schemas.Play)
async def update_play(play_id: int, play_data: schemas.PlayUpdate, db: Session = Depends(get_db)):
    return PlayServices.update_play(db, play_id, play_data)

@play_router.patch("/{play_id}", response_model=schemas.Play)
async def partial_update_play(play_id: int, play_data: schemas.PlayUpdate, db: Session = Depends(get_db)):
    return PlayServices.partial_update_play(db, play_id, play_data)

@play_router.delete("/{play_id}")
async def delete_play(play_id: int, db: Session = Depends(get_db)):
    PlayServices.delete_play(db, play_id)
    return {"detail": "Play deleted successfully"}
