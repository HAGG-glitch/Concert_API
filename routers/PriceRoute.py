from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from crud import PriceServices

price_router = APIRouter(prefix="/price", tags= ["Price"])

@price_router.post("/", response_model= schemas.Price)
async def create_price(price: schemas.CreatePrice,
                       db: Session = Depends(get_db)):
    return PriceServices.create_price(db, price)

@price_router.get("/", response_model=list[schemas.Price])
async def get_all_prices(db: Session = Depends(get_db)):
    return PriceServices.get_all_prices(db)

@price_router.get("/{price_id}", response_model=schemas.Price)
async def get_price(price_id: int, db: Session = Depends(get_db)):
    price = PriceServices.get_price(db, price_id)
    if price is None:
        raise HTTPException(status_code=404, detail="Price not found")
    return price

@price_router.put("/{price_id}", response_model=schemas.Price)
async def update_price(price_id: int, price_data: schemas.UpdatePrice, db: Session = Depends(get_db)):
    return PriceServices.update_price(db, price_id, price_data)

@price_router.patch("/{price_id}", response_model=schemas.Price)
async def partial_update_price(price_id: int, price_data: schemas.UpdatePrice, db: Session = Depends(get_db)):
    return PriceServices.partial_update_price(db, price_id, price_data)

@price_router.delete("/{price_id}")
async def delete_price(price_id: int, db: Session = Depends(get_db)):
    PriceServices.delete_price(db, price_id)
    return {"detail": "Price deleted successfully"}
