from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

book_genre_association = Table(
    'book_genre', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Integer)
    page_count = Column(Integer)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User", back_populates="books")
    genres = relationship("Genre", secondary=book_genre_association, back_populates="books")
    reservations = relationship("Reservation", back_populates="book")
