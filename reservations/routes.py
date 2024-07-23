from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db, SessionLocal
from . import crud, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Reservation])
def read_reservations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reservations = crud.get_reservations(db, skip=skip, limit=limit)
    return reservations

@router.get("/{reservation_id}", response_model=schemas.Reservation)
def read_reservation(reservation_id: int, db: Session = Depends(get_db)):
    db_reservation = crud.get_reservation(db, reservation_id=reservation_id)
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation

@router.post("/")
async def create_reservation(reservation: schemas.ReservationCreate):
    db: Session = SessionLocal()
    try:
        return crud.create_reservation(db=db, reservation=reservation)
    except ValueError as e:
        db.close()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@router.put("/{reservation_id}", response_model=schemas.Reservation)
def update_reservation(reservation_id: int, reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
    return crud.update_reservation(db=db, reservation_id=reservation_id, reservation=reservation)

@router.delete("/{reservation_id}", response_model=schemas.Reservation)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return crud.delete_reservation(db=db, reservation_id=reservation_id)
