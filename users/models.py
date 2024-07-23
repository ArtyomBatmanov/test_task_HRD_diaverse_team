from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    avatar = Column(String)

    books = relationship("Book", back_populates="author")
    reservations = relationship("Reservation", back_populates="user")
