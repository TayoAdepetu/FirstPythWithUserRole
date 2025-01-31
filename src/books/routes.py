from fastapi import APIRouter, status, Header
from fastapi.exceptions import HTTPException
from src.books.book_data import books
from src.books.schemas import BookCreateModel

from typing import List, Optional

book_router = APIRouter()

@book_router.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}


@book_router.get("/greet/{name}")
def greet(name: str) -> dict:
    return {"message": f"How are you doing, {name}"}


@book_router.get("/greet")
def greet_query(name: str) -> dict:
    return {"message": f"How are you doing, {name}"}


@book_router.get("/regreet/{name}")
def greet_query(name: str, age: int) -> dict:
    return {
        "message": f"How are you doing, {name}. I heard you are {age} years old. Is that true?"
    }


@book_router.get("/optionalgreet")
async def greet_query(name: Optional[str] = "TheTayo", age: int = 0) -> dict:
    return {
        "message": f"How are you doing, {name}. I heard you are {age} years old. Is that true?"
    }


@book_router.post("/create_book")
async def create_book(book_data: BookCreateModel) -> dict:
    return {"title": book_data.title, "author": book_data.author}


@book_router.get("/get_headers", status_code=201)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
) -> dict:
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host

    return request_headers
