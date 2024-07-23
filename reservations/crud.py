from sqlalchemy.orm import Session
from . import models, schemas

def get_reservations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Reservation).offset(skip).limit(limit).all()

def get_reservation(db: Session, reservation_id: int):
    return db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()


def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    overlapping_reservations = db.query(models.Reservation).filter(
        models.Reservation.book_id == reservation.book_id,
        models.Reservation.start_date <= reservation.end_date,
        models.Reservation.end_date >= reservation.start_date
    ).all()

    if overlapping_reservations:
        raise ValueError("The book is already reserved for the selected date range.")

    # Создание нового бронирования
    db_reservation = models.Reservation(
        book_id=reservation.book_id,
        user_id=reservation.user_id,
        start_date=reservation.start_date,
        end_date=reservation.end_date
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def update_reservation(db: Session, reservation_id: int, reservation: schemas.ReservationCreate):
    db_reservation = db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()
    if db_reservation:
        for key, value in reservation.dict().items():
            setattr(db_reservation, key, value)
        db.commit()
        db.refresh(db_reservation)
    return db_reservation

def delete_reservation(db: Session, reservation_id: int):
    db_reservation = db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()
    if db_reservation:
        db.delete(db_reservation)
        db.commit()
    return db_reservation
