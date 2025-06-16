from sqlalchemy.orm import Session
from fastapi import  HTTPException
import schemas
from typing import Optional, List
from models import Customer
from datetime import date


def create_customer(db: Session, customer_data: schemas.CreateCustomer):
    customer = Customer(
        name = customer_data.name,
        telephone = customer_data.telephone

    )

    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_customer_by_name(db: Session, name: str) -> Optional[Customer]:
    return db.query(Customer).filter(Customer.name == name).first()

def get_all_customers(db: Session) -> List[type[Customer]]:
    return db.query(Customer).all()

def get_customer(db: Session, customer_id: int) -> Optional[Customer]:
    return db.query(Customer).filter(Customer.id == customer_id).first()

def update_customer(db: Session, customer_id: int, customer_data: schemas.UpdateCustomer) ->Customer:
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code= 404, detail= "Customer not found")
    customer.name = customer_data.name
    customer.telephone = customer_data.telephone
    db.commit()
    db.refresh(customer)
    return customer

def partial_update_customer(db:Session, customer_id: int,customer_data: schemas.UpdateCustomer ) -> Customer:
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    if customer_data.name is not None:
        customer.name = customer_data.name
    if customer_data.telephone is not None:
        customer.telephone = customer_data.telephone
    db.commit()
    db.refresh(customer)
    return customer

def delete_customer (db: Session,  customer_id: int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()



