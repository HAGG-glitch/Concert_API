from sqlalchemy.orm import Session

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
