from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from database import  get_db

import schemas

from services import TicketServices

ticket_router = APIRouter(prefix="/ticket", tags= ["Tickets"])

@ticket_router.post("/", response_model= schemas.Ticket)
async def create_ticket(ticket: schemas.CreateTicket,
                       db: Session = Depends(get_db)):
    return TicketServices.create_ticket(db, ticket)