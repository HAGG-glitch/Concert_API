from __future__ import annotations
from datetime import date
from typing import Optional

from pydantic import BaseModel


# ---------- PLAY ----------
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
        orm_mode = True


# ---------- ACTOR ----------
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
        orm_mode = True


# ---------- ACTOR-PLAY LINK ----------
class ActorPlayBase(BaseModel):
    actor_id: int
    play_id: int

class CreateActorPlay(ActorPlayBase):
    pass

class ActorPlay(ActorPlayBase):
    id: int
    class Config:
        orm_mode = True


# ---------- DIRECTOR ----------
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
        orm_mode = True


# ---------- DIRECTOR-PLAY LINK ----------
class DirectorPlayBase(BaseModel):
    director_id: int
    play_id: int

class CreateDirectorPlay(DirectorPlayBase):
    pass

class DirectorPlay(DirectorPlayBase):
    id: int
    class Config:
        orm_mode = True


# ---------- SEAT ----------
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
        orm_mode = True


# ---------- SHOWTIME ----------
class ShowTimeBase(BaseModel):
    date: date
    play_id: int

class CreateShowTime(ShowTimeBase):
    pass

class UpdateShowTime(BaseModel):
    date: Optional[date] = None
    play_id: Optional[int] = None

class ShowTime(ShowTimeBase):
    id: int
    class Config:
        orm_mode = True


# ---------- CUSTOMER ----------
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
        orm_mode = True


# ---------- PRICE ----------
class PriceBase(BaseModel):
    seat_id: int
    showtime_id: int
    price: float

class CreatePrice(PriceBase):
    pass

class UpdatePrice(BaseModel):
    seat_id: Optional[int] = None
    showtime_id: Optional[int] = None
    price: Optional[float] = None

class Price(PriceBase):
    id: int
    class Config:
        orm_mode = True


# ---------- TICKET ----------
class TicketBase(BaseModel):
    ticket_no: Optional[str]
    seat_id: int
    showtime_id: int
    customer_id: int

class CreateTicket(TicketBase):
    pass

class UpdateTicket(BaseModel):
    ticket_no: Optional[str] = None

class Ticket(TicketBase):
    id: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
