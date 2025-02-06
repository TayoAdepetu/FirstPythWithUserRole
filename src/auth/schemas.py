from pydantic import BaseModel, Field
from sqlmodel import Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid
from typing import List
from src.books.schemas import Book
from src.reviews.schemas import ReviewModel

class UserCreateModel(BaseModel):
    username: str = Field(max_length=15)
    email: str = Field(max_length=40)
    password: str = Field(min_length=26)
    first_name: str
    last_name: str


class UserModel(BaseModel):
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    username: str
    first_name: str
    last_name: str
    password_hash: str = Field(exclude=True)
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    
    
class UserBooksModel(UserModel):
    books: List[Book] 
    reviews: List[ReviewModel]


class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=26)
