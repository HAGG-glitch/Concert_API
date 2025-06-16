from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from crud import DirectorServices

director_router = APIRouter(prefix="/director", tags= ["Director"])

@director_router.post("/", response_model= schemas.Director)
async def create_director(director: schemas.CreateDirector,
                       db: Session = Depends(get_db)):
    return DirectorServices.create_director(db, director)

@director_router.get("/", response_model=list[schemas.Director])
def get_all_directors(db: Session = Depends(get_db)):
    return DirectorServices.get_all_directors(db)

@director_router.get("/{director_id}", response_model=schemas.Director)
def get_director(director_id: int, db: Session = Depends(get_db)):
    db_director = DirectorServices.get_director(db, director_id)
    if not db_director:
        raise HTTPException(status_code=404, detail="Director not found")
    return db_director

@director_router.put("/{director_id}", response_model=schemas.Director)
async def update_director(director_id: int, director_data: schemas.UpdateDirector, db: Session = Depends(get_db)):
    return DirectorServices.update_director(db, director_id, director_data)

@director_router.patch("/{director_id}", response_model=schemas.Director)
async def partial_update_director(director_id: int, director_data: schemas.UpdateDirector, db: Session = Depends(get_db)):
    return DirectorServices.partial_update_director(db,director_id, director_data)


@director_router.delete("/{director_id}")
def remove_director(director_id: int, db: Session = Depends(get_db)):
    return DirectorServices.delete_director(db, director_id)