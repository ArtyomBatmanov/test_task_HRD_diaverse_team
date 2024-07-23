from pydantic import BaseModel
from datetime import date

class ReservationBase(BaseModel):
    book_id: int
    user_id: int
    start_date: date
    end_date: date

class ReservationCreate(BaseModel):
    book_id: int
    user_id: int
    start_date: date
    end_date: date

    class Config:
        from_attributes = True


class Reservation(ReservationBase):
    id: int

    class Config:
        from_attributes = True
