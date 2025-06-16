from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import CreateTicket, TicketBase  # adjust ShowTicket to match your output schema
from crud.booking_tickets import book_ticket  # the service function you just finalized

router = APIRouter(
    prefix="/booking",
    tags=["Ticket Booking"]
)

@router.post("/", response_model=TicketBase, status_code=status.HTTP_201_CREATED)
def book_new_ticket(
    ticket_data: CreateTicket,
    customer_id: int,
    db: Session = Depends(get_db)
):
    """
    Endpoint to book a new ticket for a customer.
    Ensures seat and showtime exist and the seat is not already booked.
    """
    try:
        ticket = book_ticket(db, ticket_data, customer_id)
        return ticket
    except HTTPException as e:
        raise e
