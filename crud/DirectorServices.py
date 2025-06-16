from fastapi import HTTPException
from sqlalchemy.orm import Session

import schemas
from typing import Optional, List
from models import Director
from datetime import date


def create_director(db: Session, director_data: schemas.CreateDirector):
    director = Director(
        name = director_data.name,
        dob = director_data.dob,
        citizenship = director_data.citizenship,
    )

    db.add(director)
    db.commit()
    db.refresh(director)
    return director

def get_all_directors(db: Session)-> List[type[Director]]:
    return db.query(Director).all()

def get_director (db: Session, director_id: int) -> Optional[Director]:
    return db.query(Director).filter(Director.id == director_id).first()

def update_director(db: Session, director_id: int, director_data: schemas.UpdateDirector) -> Director:
    director = db.query(Director).filter(Director.id == director_id).first()
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    director.name = director_data.name
    director.dob = director_data.dob
    director.citizenship = director_data.citizenship
    db.commit()
    db.refresh(director)
    return director

def partial_update_director(db: Session, director_id: int, director_data: schemas.UpdateDirector) -> Director:
    director = db.query(Director).filter(Director.id == director_id).first()
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    if director_data.name is not None:
        director.name = director_data.name
    if director.dob is not None:
        director.dob = director_data.dob
    if director.citizenship is not None:
        director.citizenship = director_data.citizenship
    db.commit()
    db.refresh(director)
    return director


def delete_director (db: Session, director_id: int):
    director = db.query(Director).filter(Director.id == director_id).first()
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    db.delete(director)
    db.commit()