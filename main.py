from fastapi import FastAPI
from routers import  ActorRoute, ActorPlayRoute, CustomerRoute, DirectorRoute, DirectorPlayRoute, PlayRoute, PriceRoute, SeatRoute, ShowTimeRoute, TicketRoute,auth, booking_ticket_router
from fastapi.middleware.cors import CORSMiddleware
from database import Session_Local, engine, Base
from security.auth_service import get_current_user


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Theater Booking API",
    description="API for managing plays, actors, directors, tickets, and customers",
    docs_url="/docs",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = Session_Local()
    try:
        yield db
    finally:
        db.close()

app.include_router(ActorRoute.actor_router)
app.include_router(ActorPlayRoute.actorplay_router)
app.include_router(CustomerRoute.customer_router)
app.include_router(DirectorRoute.director_router)
app.include_router(DirectorPlayRoute.directorplay_router)
app.include_router(PlayRoute.play_router)
app.include_router(PriceRoute.price_router)
app.include_router(SeatRoute.seat_router)
app.include_router(ShowTimeRoute.showtime_router)
app.include_router(TicketRoute.ticket_router)
app.include_router(auth.auth_router)
app.include_router(booking_ticket_router.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Theater Booking API "}