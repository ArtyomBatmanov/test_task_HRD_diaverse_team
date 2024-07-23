from pydantic import BaseModel
from typing import List

class BookBase(BaseModel):
    title: str
    price: float
    page_count: int
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    genres: List[int] = []

    class Config:
        from_attributes = True
