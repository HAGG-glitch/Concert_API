

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from routers import (
    ActorRoute,
    ActorPlayRoute,
    CustomerRoute,
    DirectorRoute,
    DirectorPlayRoute,
    PlayRoute,
    PriceRoute,
    SeatRoute,
    ShowTimeRoute,
    TicketRoute,
    auth,
    booking_ticket_router,
    user_routers
)

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Concert Ticket Booking API",
    description="Manage concerts, bookings, actors, directors, users with authentication and advanced features.",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.auth_router)
app.include_router(user_routers.user_router, prefix="/users", tags=["Users"])
app.include_router(PlayRoute.play_router, prefix="/plays", tags=["Plays"])
app.include_router(DirectorRoute.director_router, prefix="/directors", tags=["Directors"])
app.include_router(DirectorPlayRoute.directorplay_router, prefix="/directorplays", tags=["Directorplays"])
app.include_router(ActorRoute.actor_router, prefix="/actors", tags=["Actors"])
app.include_router(ActorPlayRoute.actorplay_router, prefix="/actorplays", tags=["Actorplays"])
app.include_router(ShowTimeRoute.showtime_router, prefix="/showtimes", tags=["Showtimes"])
app.include_router(TicketRoute.ticket_router, prefix="/tickets", tags=["Tickets"])
app.include_router(SeatRoute.seat_router, prefix="/seats", tags=["Seats"])
app.include_router(PriceRoute.price_router, prefix="/prices", tags=["Prices"])
app.include_router(CustomerRoute.customer_router, prefix="/customers", tags=["Customers"])
app.include_router(booking_ticket_router.router, prefix="/booktickets", tags=["BookTickets"])
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "🎟️ Welcome to the Concert Ticket Booking API"}
