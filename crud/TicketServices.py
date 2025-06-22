from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Optional, List
from datetime import date

from models import Ticket
import schemas

def create_ticket(db: Session, ticket_data: schemas.CreateTicket) -> Ticket:
    ticket = Ticket(
        ticket_no=ticket_data.ticket_no,
        seat_id=ticket_data.seat_id,
        showtime_id=ticket_data.showtime_id,
        customer_id=ticket_data.customer_id,
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def get_all_tickets(db: Session) -> list[type[Ticket]]:
    return db.query(Ticket).all()

def get_ticket_by_id(db: Session, ticket_id: int) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

def get_ticket_by_ticket_no(db: Session, ticket_no: str) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.ticket_no == ticket_no).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

def partial_update_ticket(db:Session, ticket_id: int, ticket_data: schemas.UpdateTicket) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    if ticket_data.ticket_no is not None:
        ticket.ticket_no = ticket_data.ticket_no
    db.commit()
    db.refresh(ticket)
    return ticket

def update_ticket(db: Session, ticket_id: int, ticket_update: schemas.UpdateTicket) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    update_data = ticket_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(ticket, key, value)

    db.commit()
    db.refresh(ticket)
    return ticket

def delete_ticket(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.delete(ticket)
    db.commit()

def book_ticket(db: Session, ticket_data: schemas.CreateTicket, customer_id: int) -> Ticket:
    # Check if seat exists
    seat = db.query(schemas.Seat).filter(schemas.Seat.id == ticket_data.seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")

    # Check if showtime exists
    showtime = db.query(schemas.ShowTime).filter(schemas.ShowTime.id == ticket_data.showtime_id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")

    # Check if customer exists
    customer = db.query(schemas.Customer).filter(schemas.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Check if seat is already booked for this showtime
    existing_ticket = db.query(Ticket).filter(
        Ticket.seat_id == ticket_data.seat_id,
        Ticket.showtime_id == ticket_data.showtime_id
    ).first()
    if existing_ticket:
        raise HTTPException(status_code=400, detail="Seat already booked for this showtime")

    # Create the ticket
    new_ticket = Ticket(
        ticket_no=ticket_data.ticket_no,
        seat_id=ticket_data.seat_id,
        showtime_id=ticket_data.showtime_id,
        customer_id=customer_id
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

