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
