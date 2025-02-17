from pydantic import BaseModel
from datetime import datetime, date
import uuid
from typing import List
from src.reviews.schemas import ReviewModel

# model format to create
class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

# model format to retrieve
class Book(BaseModel):
    id: int
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime

# model format to update
class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookDetailModel(Book):
    reviews:List[ReviewModel]