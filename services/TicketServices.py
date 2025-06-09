from sqlalchemy.orm import Session

import schemas
from typing import Optional, List
from models import Ticket
from datetime import date


def create_ticket(db: Session, ticket_data: schemas.CreateTicket):
    ticket = Ticket(
        seat_row_no = ticket_data.seat_row_no,
        seat_seat_no = ticket_data.seat_seat_no,
        showtime_date_time = ticket_data.showtime_date_time,
        showtime_play_id = ticket_data.showtime_play_id,
        customer_id = ticket_data.customer_id,
        ticket_no = ticket_data.ticket_no
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket
