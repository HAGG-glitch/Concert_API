from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime

# ------------------- Play -------------------
class PlayBase(BaseModel):
    title: str
    duration: int
    genre: str
    synopsis: Optional[str] = None

class PlayCreate(PlayBase):
    pass

class PlayUpdate(BaseModel):
    title: Optional[str] = None
    duration: Optional[int] = None
    genre: Optional[str] = None
    synopsis: Optional[str] = None

class Play(PlayBase):
    id: int

    class Config:
        form_attributes = True

# ------------------- Actor -------------------
class ActorBase(BaseModel):
    name: str
    gender: str
    dob: date

class CreateActor(ActorBase):
    pass

class UpdateActor(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[date] = None

class Actor(ActorBase):
    id: int

    class Config:
        form_attributes = True

# ------------------- ActorPlay -------------------
class ActorPlay(BaseModel):
    actor_id: int
    play_id: int

    class Config:
        form_attributes = True

# ------------------- Director -------------------
class DirectorBase(BaseModel):
    name: str
    dob: date
    citizenship: str

class CreateDirector(DirectorBase):
    pass

class UpdateDirector(BaseModel):
    name: Optional[str] = None
    dob: Optional[date] = None
    citizenship: Optional[str] = None

class Director(DirectorBase):
    id: int

    class Config:
        form_attributes = True

# ------------------- DirectorPlay -------------------
class DirectorPlay(BaseModel):
    director_id: int
    play_id: int

    class Config:
        form_attributes = True

# ------------------- ShowTime -------------------
class ShowTimeBase(BaseModel):
    date_time: datetime
    play_id: int

class CreateShowTime(ShowTimeBase):
    pass

class UpdateShowTime(BaseModel):
    date_time: Optional[datetime] = None
    play_id: Optional[int] = None

class ShowTime(ShowTimeBase):
    id: int

    class Config:
        form_attributes = True

# ------------------- Seat -------------------
class SeatBase(BaseModel):
    row_no: int
    seat_no: int

class CreateSeat(SeatBase):
    pass

class UpdateSeat(BaseModel):
    row_no: Optional[int] = None
    seat_no: Optional[int] = None

class Seat(SeatBase):
    id: int

    class Config:
        form_attributes = True

# ------------------- Customer -------------------
class CustomerBase(BaseModel):
    name: str
    telephone: str

class CreateCustomer(CustomerBase):
    pass

class UpdateCustomer(BaseModel):
    name: Optional[str] = None
    telephone: Optional[str] = None

class Customer(CustomerBase):
    id: int

    class Config:
        form_attributes = True

# ------------------- Price -------------------
class PriceBase(BaseModel):
    seat_row_no: int
    seat_seat_no: int
    showtime_date_time: datetime
    showtime_play_id: int
    price: float

class CreatePrice(PriceBase):
    pass

class UpdatePrice(BaseModel):
    seat_row_no: Optional[int] = None
    seat_seat_no: Optional[int] = None
    showtime_date_time: Optional[datetime] = None
    showtime_play_id: Optional[int] = None
    price: Optional[float] = None

class Price(PriceBase):
    id: int

    class Config:
        form_attributes = True

# ------------------- Ticket -------------------
class TicketBase(BaseModel):
    seat_row_no: int
    seat_seat_no: int
    showtime_date_time: datetime
    showtime_play_id: int
    customer_id: int
    ticket_no: Optional[str] = None

class CreateTicket(TicketBase):
    pass

class UpdateTicket(BaseModel):
    seat_row_no: Optional[int] = None
    seat_seat_no: Optional[int] = None
    showtime_date_time: Optional[datetime] = None
    showtime_play_id: Optional[int] = None
    customer_id: Optional[int] = None
    ticket_no: Optional[str] = None

class Ticket(TicketBase):
    id: int

    class Config:
        form_attributes = True

# ------------------- Relations -------------------
class PlayWithRelations(Play):
    director: Optional[Director]
    showtimes: List[ShowTime] = []
    actors: List[Actor] = []

class ActorWithRelations(Actor):
    plays: List[Play] = []

class DirectorWithRelations(Director):
    plays: List[Play] = []

class ShowTimeWithRelations(ShowTime):
    play: Play
    tickets: List[Ticket] = []
    prices: List[Price] = []

class SeatWithRelations(Seat):
    tickets: List[Ticket] = []
    prices: List[Price] = []

class CustomerWithRelations(Customer):
    tickets: List[Ticket] = []

class PriceWithRelations(Price):
    seat: Seat
    showtime: ShowTime

class TicketWithRelations(Ticket):
    seat: Seat
    showtime: ShowTime
    customer: Customer
