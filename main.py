from fastapi import FastAPI
from database import engine, Base
from books import routes as book_routes
from users import routes as user_routes
from genres import routes as genre_routes
from reservations import routes as reservation_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(book_routes.router, prefix="/books", tags=["books"])
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(genre_routes.router, prefix="/genres", tags=["genres"])
app.include_router(reservation_routes.router, prefix="/reservations", tags=["reservations"])
