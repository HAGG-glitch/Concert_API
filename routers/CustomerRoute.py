from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from crud import CustomerServices

customer_router = APIRouter(prefix="/customer", tags= ["Customer"])

@customer_router.post("/", response_model= schemas.Customer)
async def create_customer(customer: schemas.CreateCustomer,
                       db: Session = Depends(get_db)):
    return CustomerServices.create_customer(db, customer)

@customer_router.get("/", response_model=list[schemas.Customer])
def get_all_customers(db: Session = Depends(get_db)):
    return CustomerServices.get_all_customers(db)

@customer_router.get("/{customer_id}", response_model=schemas.Customer)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = CustomerServices.get_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@customer_router.put("/{customer_id}", response_model=schemas.Customer)
async def update_customer(customer_id: int, customer_data: schemas.UpdateCustomer, db: Session = Depends(get_db)):
    return CustomerServices.update_customer(db, customer_id, customer_data)

@customer_router.patch("/{customer_id}", response_model=schemas.Customer)
async def partial_update_customer(customer_id: int, customer_data: schemas.UpdateCustomer, db: Session = Depends(get_db)):
    return CustomerServices.partial_update_customer(db,customer_id, customer_data)


@customer_router.delete("/{customer_id}")
def remove_customer(customer_id: int, db: Session = Depends(get_db)):
    return CustomerServices.delete_customer(db, customer_id)