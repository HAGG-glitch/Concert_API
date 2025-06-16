from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

import schemas
from crud import TicketServices
from database import get_db

ticket_router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

@ticket_router.post("/", response_model=schemas.Ticket)
async def create_ticket(ticket: schemas.CreateTicket, db: Session = Depends(get_db)):
    return TicketServices.create_ticket(db, ticket)

@ticket_router.get("/", response_model=list[schemas.Ticket])
async def get_all_tickets(db: Session = Depends(get_db)):
    return TicketServices.get_all_tickets(db)

@ticket_router.get("/{ticket_id}", response_model=schemas.Ticket)
async def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = TicketServices.get_ticket_by_id(db, ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@ticket_router.put("/{ticket_id}", response_model=schemas.Ticket)
async def update_ticket(ticket_id: int, ticket_data: schemas.UpdateTicket, db: Session = Depends(get_db)):
    return TicketServices.update_ticket(db, ticket_id, ticket_data)

@ticket_router.patch("/{ticket_id}", response_model=schemas.Ticket)
async def partial_update_ticket(ticket_id: int, ticket_data: schemas.UpdateTicket, db: Session = Depends(get_db)):
    return TicketServices.partial_update_ticket(db, ticket_id, ticket_data)

@ticket_router.delete("/{ticket_id}")
async def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    TicketServices.delete_ticket(db, ticket_id)
    return {"detail": "Ticket deleted successfully"}
