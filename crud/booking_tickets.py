from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from crud import TicketServices as ticket_crud
from crud import SeatServices as seat_crud
from crud import ShowTimeServices as showtime_crud
from crud import CustomerServices as customer_crud
from models import Ticket
from schemas import CreateTicket as TicketCreate

def book_ticket(
    db: Session,
    ticket_in: TicketCreate,
    customer_id: int
) -> Ticket:
    """
    Book a ticket if the seat and showtime are valid and the seat is not already booked for the showtime.
    """

    # ✅ 1. Verify seat exists
    seat = seat_crud.get_seat_by_id(db, ticket_in.seat_id)
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")

    # ✅ 2. Verify showtime exists
    showtime = showtime_crud.get_showtime_by_id(db, ticket_in.showtime_id)
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")

    # ✅ 3. Verify customer exists
    customer = customer_crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # ✅ 4. Check if seat already booked for this showtime (by anyone)
    existing_ticket = db.query(Ticket).filter(
        Ticket.seat_id == ticket_in.seat_id,
        Ticket.showtime_id == ticket_in.showtime_id,
    ).first()

    if existing_ticket:
        raise HTTPException(status_code=400, detail="Seat already booked for this showtime")

    # ✅ 5. Proceed to create the ticket
    new_ticket_data = TicketCreate(
        ticket_no=ticket_in.ticket_no,
        seat_id=ticket_in.seat_id,
        showtime_id=ticket_in.showtime_id,
        customer_id=customer_id
    )

    ticket = ticket_crud.create_ticket(db, new_ticket_data)
    return ticket
