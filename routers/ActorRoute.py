from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schemas
from crud import ActorServices

actor_router = APIRouter(prefix="/actor", tags=["Actor"])

@actor_router.post("/", response_model=schemas.Actor)
async def create_actor(actor: schemas.CreateActor, db: Session = Depends(get_db)):
    return ActorServices.create_actor(db, actor)

@actor_router.get("/", response_model=list[schemas.Actor])
async def get_all_actors(db: Session = Depends(get_db)):
    return ActorServices.get_all_actors(db)

@actor_router.get("/{actor_id}", response_model=schemas.Actor)
async def get_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = ActorServices.get_actor(db, actor_id)
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@actor_router.put("/{actor_id}", response_model=schemas.Actor)
async def update_actor(actor_id: int, actor_data: schemas.UpdateActor, db: Session = Depends(get_db)):
    return ActorServices.update_actor(db, actor_id, actor_data)

@actor_router.patch("/{actor_id}", response_model=schemas.Actor)
async def partial_update_actor(actor_id: int, actor_data: schemas.UpdateActor, db: Session = Depends(get_db)):
    return ActorServices.partial_update_actor(db, actor_id, actor_data)

@actor_router.delete("/{actor_id}")
async def delete_actor(actor_id: int, db: Session = Depends(get_db)):
    ActorServices.delete_actor(db, actor_id)
    return {"detail": "Actor deleted successfully"}
