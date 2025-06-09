from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from services import CustomerServices

customer_router = APIRouter(prefix="/customer", tags= ["Customer"])

@customer_router.post("/", response_model= schemas.Customer)
async def create_customer(customer: schemas.CreateCustomer,
                       db: Session = Depends(get_db)):
    return CustomerServices.create_customer(db, customer)