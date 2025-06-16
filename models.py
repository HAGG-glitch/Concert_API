from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

# ---------- PLAY ----------
class Play(Base):
    __tablename__ = "plays"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    duration = Column(Integer, nullable=False)
    genre = Column(String, index=True)
    synopsis = Column(Text)

    showtimes = relationship("ShowTime", back_populates="play")
    actor_links = relationship("ActorPlay", back_populates="play")
    director_links = relationship("DirectorPlay", back_populates="play")


# ---------- ACTOR ----------
class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    gender = Column(String)
    dob = Column(Date)

    actor_links = relationship("ActorPlay", back_populates="actor")


# ---------- ACTOR-PLAY LINK ----------
class ActorPlay(Base):
    __tablename__ = "actor_play"
    id = Column(Integer, primary_key=True, index=True)
    actor_id = Column(Integer, ForeignKey("actors.id"))
    play_id = Column(Integer, ForeignKey("plays.id"))

    actor = relationship("Actor", back_populates="actor_links")
    play = relationship("Play", back_populates="actor_links")


# ---------- DIRECTOR ----------
class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    dob = Column(Date)
    citizenship = Column(String)

    director_links = relationship("DirectorPlay", back_populates="director")


# ---------- DIRECTOR-PLAY LINK ----------
class DirectorPlay(Base):
    __tablename__ = "director_play"
    id = Column(Integer, primary_key=True, index=True)
    director_id = Column(Integer, ForeignKey("directors.id"))
    play_id = Column(Integer, ForeignKey("plays.id"))

    director = relationship("Director", back_populates="director_links")
    play = relationship("Play", back_populates="director_links")


# ---------- SEAT ----------
class Seat(Base):
    __tablename__ = "seats"
    id = Column(Integer, primary_key=True, index=True)
    row_no = Column(Integer)
    seat_no = Column(Integer)

    tickets = relationship("Ticket", back_populates="seat")
    prices = relationship("Price", back_populates="seat")


# ---------- SHOWTIME ----------
class ShowTime(Base):
    __tablename__ = "show_times"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    play_id = Column(Integer, ForeignKey("plays.id"))

    tickets = relationship("Ticket", back_populates="showtime")
    prices = relationship("Price", back_populates="showtime")
    play = relationship("Play", back_populates="showtimes")


# ---------- CUSTOMER ----------
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    telephone = Column(String)

    tickets = relationship("Ticket", back_populates="customer")


# ---------- PRICE ----------
class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, index=True)
    seat_id = Column(Integer, ForeignKey("seats.id"))
    showtime_id = Column(Integer, ForeignKey("show_times.id"))
    price = Column(Float, nullable=False)

    seat = relationship("Seat", back_populates="prices")
    showtime = relationship("ShowTime", back_populates="prices")


# ---------- TICKET ----------
class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    ticket_no = Column(String(10), nullable=False, unique=True)
    seat_id = Column(Integer, ForeignKey("seats.id"))
    showtime_id = Column(Integer, ForeignKey("show_times.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))

    seat = relationship("Seat", back_populates="tickets")
    showtime = relationship("ShowTime", back_populates="tickets")
    customer = relationship("Customer", back_populates="tickets")
