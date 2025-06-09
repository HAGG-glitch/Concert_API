from sqlalchemy import Column, Integer,Float, String, Text, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from database import Base

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

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    gender = Column(String)
    dob = Column(Date)

    plays = relationship("ActorPlay", back_populates="actor")

class ActorPlay(Base):
    __tablename__ = "actor_play"
    actor_id = Column(Integer, ForeignKey("actors.id"), primary_key=True)
    play_id = Column(Integer, ForeignKey("plays.id"), primary_key=True)

    actor = relationship("Actor", back_populates="plays")
    play = relationship("Play", back_populates="actor_links")

class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    dob = Column(Date)
    citizenship = Column(String)

    plays = relationship("DirectorPlay", back_populates="director")

class DirectorPlay(Base):
    __tablename__ = "director_play"
    director_id = Column(Integer, ForeignKey("directors.id"), primary_key=True)
    play_id = Column(Integer, ForeignKey("plays.id"), primary_key=True)

    director = relationship("Director", back_populates="plays")
    play = relationship("Play", back_populates="director_links")



class ShowTime(Base):
    __tablename__ = "show_times"
    date_time = Column(DateTime, primary_key=True)
    play_id = Column(Integer, ForeignKey("plays.id"), primary_key=True)

    play = relationship("Play", back_populates="showtimes")
    tickets = relationship("Ticket", back_populates="showtime")
    prices = relationship("Price", back_populates="showtime")

class Seat(Base):
    __tablename__ = "seats"
    row_no = Column(Integer, primary_key=True)
    seat_no = Column(Integer, primary_key=True)

    tickets = relationship("Ticket", back_populates="seat")
    prices = relationship("Price", back_populates="seat")

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    telephone = Column(String)

    tickets = relationship("Ticket", back_populates="customer")

class Price(Base):
    __tablename__ = "prices"
    seat_row_no = Column(Integer, ForeignKey("seats.row_no"), primary_key=True)
    seat_seat_no = Column(Integer, ForeignKey("seats.seat_no"), primary_key=True)
    showtime_date_time = Column(DateTime, primary_key=True)
    showtime_play_id = Column(Integer, primary_key=True)
    price = Column(Float)

    seat = relationship("Seat", back_populates="prices")
    showtime = relationship("ShowTime", back_populates="prices",
        primaryjoin="and_(Price.showtime_date_time==ShowTime.date_time, Price.showtime_play_id==ShowTime.play_id)"
    )

class Ticket(Base):
    __tablename__ = "tickets"
    seat_row_no = Column(Integer, ForeignKey("seats.row_no"), primary_key=True)
    seat_seat_no = Column(Integer, ForeignKey("seats.seat_no"), primary_key=True)
    showtime_date_time = Column(DateTime, primary_key=True)
    showtime_play_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), primary_key=True)
    ticket_no = Column(String(10), nullable=False)

    seat = relationship("Seat", back_populates="tickets")
    showtime = relationship("ShowTime", back_populates="tickets",
        primaryjoin="and_(Ticket.showtime_date_time==ShowTime.date_time, Ticket.showtime_play_id==ShowTime.play_id)"
    )
    customer = relationship("Customer", back_populates="tickets")



