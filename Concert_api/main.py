from fastapi import FastAPI
from routers import  ActorRoute, ActorPlayRoute, CustomerRoute, DirectorRoute, DirectorPlayRoute, PlayRoute, PriceRoute, SeatRoute, ShowTimeRoute, TicketRoute

app = FastAPI(title="Concert API")

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

@app.get("/")
def root():
    return {"message": "🎶 Welcome to Concert API"}