from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    books = relationship("Book", secondary='book_genre', back_populates="genres")
