from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from services import PriceServices

price_router = APIRouter(prefix="/price", tags= ["Price"])

@price_router.post("/", response_model= schemas.Price)
async def create_price(price: schemas.CreatePrice,
                       db: Session = Depends(get_db)):
    return PriceServices.create_price(db, price)