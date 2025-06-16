from sqlalchemy.orm import Session
from fastapi import HTTPException
import schemas
from typing import Optional, List
from models import Price
from datetime import date


def create_price(db: Session, price_data: schemas.CreatePrice):
    price = Price(
        seat_id = price_data.seat_id,
        showtime_id = price_data.showtime_id,
        price = price_data.price
    )
    db.add(price)
    db.commit()
    db.refresh(price)
    return price

def get_all_prices(db: Session) -> List[type[Price]]:
    return db.query(Price).all()

def get_price(db: Session, price_id: int) -> Optional[Price]:
    return db.query(Price).filter(Price.id == price_id).first()

def update_price(db: Session, price_id:int, price_data: schemas.UpdatePrice) -> Price:
    price = db.query(Price).filter(Price.id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    price.seat_id = price_data.seat_id
    price.seat_showtime_id = price_data.showtime_id
    price.price = price_data.price
    db.commit()
    db.refresh(price)
    return price


def partial_update_price(db: Session, price_id:int, price_data: schemas.UpdatePrice) -> Price:
    price = db.query(Price).filter(Price.id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    if price_data.seat_id is not None:
        price.seat_id = price_data.seat_id
    if price_data.showtime_id is not None:
        price.showtime_id = price_data.showtime_id
    if price_data.price is not None:
        price.price = price_data.price
    db.commit()
    db.refresh(price)
    return price


def delete_price(db: Session, price_id: int):
    price = db.query(Price).filter(Price.id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    db.delete(price)
    db.commit()


