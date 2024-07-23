from sqlalchemy.orm import Session
from . import models, schemas
from genres.models import Genre

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        price=book.price,
        page_count=book.page_count,
        author_id=book.author_id
    )
    db_book.genres = db.query(models.Genre).filter(models.Genre.id.in_(book.genres)).all()
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book_update: schemas.BookUpdate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        return None
    if book_update.title is not None:
        db_book.title = book_update.title
    if book_update.price is not None:
        db_book.price = book_update.price
    if book_update.page_count is not None:
        db_book.page_count = book_update.page_count
    if book_update.author_id is not None:
        db_book.author_id = book_update.author_id
    if book_update.genres is not None:
        db_book.genres = db.query(models.Genre).filter(models.Genre.id.in_(book_update.genres)).all()
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book




