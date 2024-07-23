from sqlalchemy.orm import Session
from . import models, schemas

def get_genres(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Genre).offset(skip).limit(limit).all()

def get_genre(db: Session, genre_id: int):
    return db.query(models.Genre).filter(models.Genre.id == genre_id).first()

def create_genre(db: Session, genre: schemas.GenreCreate):
    db_genre = models.Genre(**genre.dict())
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre

def update_genre(db: Session, genre_id: int, genre: schemas.GenreCreate):
    db_genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
    if db_genre:
        for key, value in genre.dict().items():
            setattr(db_genre, key, value)
        db.commit()
        db.refresh(db_genre)
    return db_genre

def delete_genre(db: Session, genre_id: int):
    db_genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
    if db_genre:
        db.delete(db_genre)
        db.commit()
    return db_genre
