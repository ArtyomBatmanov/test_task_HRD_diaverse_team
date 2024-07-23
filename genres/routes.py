from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from . import crud, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Genre])
def read_genres(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    genres = crud.get_genres(db, skip=skip, limit=limit)
    return genres

@router.get("/{genre_id}", response_model=schemas.Genre)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = crud.get_genre(db, genre_id=genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre

@router.post("/", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    return crud.create_genre(db=db, genre=genre)

@router.put("/{genre_id}", response_model=schemas.Genre)
def update_genre(genre_id: int, genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    return crud.update_genre(db=db, genre_id=genre_id, genre=genre)

@router.delete("/{genre_id}", response_model=schemas.Genre)
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    return crud.delete_genre(db=db, genre_id=genre_id)
