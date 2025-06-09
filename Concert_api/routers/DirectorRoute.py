from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from services import DirectorServices

director_router = APIRouter(prefix="/director", tags= ["Director"])

@director_router.post("/", response_model= schemas.Director)
async def create_director(director: schemas.CreateDirector,
                       db: Session = Depends(get_db)):
    return DirectorServices.create_director(db, director)