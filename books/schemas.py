from pydantic import BaseModel
from typing import List, Optional

class BookBase(BaseModel):
    title: str
    price: float
    page_count: int
    author_id: int

class BookCreate(BookBase):
    genres: List[int]

class Book(BookBase):
    id: int
    genres: List[int] = []

    class Config:
        from_attributes = True



class BookUpdate(BaseModel):
    title: Optional[str] = None
    price: Optional[float] = None
    page_count: Optional[int] = None
    author_id: Optional[int] = None
    genres: Optional[List[int]] = None

    class Config:
        from_attributes = True
