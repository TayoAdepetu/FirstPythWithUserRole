from pydantic import BaseModel
from datetime import datetime
import uuid

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
    uid: uuid
    title: str
    author: str
    publisher: str
    published_date: str
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

