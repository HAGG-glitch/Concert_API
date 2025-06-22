from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import BackgroundTasks
import crud
import models
import schemas
from crud import TicketServices
from database import get_db
from security.security_roles import require_role, get_current_user
from models import Customer


ticket_router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)
@ticket_router.post("/", response_model=schemas.Ticket)
def book_ticket(
    ticket: schemas.CreateTicket,
    db: Session = Depends(get_db),
    current_user: Customer = Depends(require_role("customer"))  # Only customers can book
):
    return TicketServices.book_ticket(db, ticket, current_user.id)

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



def send_booking_email(email: str, ticket_id: int):
    # Simulate sending email
    print(f"Sending booking confirmation to {email} for ticket ID {ticket_id}")

@ticket_router.post("/", response_model=schemas.Ticket)
def create_ticket(
    ticket: schemas.CreateTicket,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    db_ticket = crud.TicketServices.create_ticket(db=db, ticket_data=ticket)

    # Get customer email
    customer = db.query(models.Customer).filter(models.Customer.id == ticket.customer_id).first()
    if customer and customer.email:
        background_tasks.add_task(send_booking_email, customer.email, db_ticket.id)

    return db_ticket

