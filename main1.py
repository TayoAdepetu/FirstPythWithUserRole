from fastapi import FastAPI, Header
from typing import Optional


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}


@app.get("/greet/{name}")
def greet(name: str) -> dict:
    return {"message": f"How are you doing, {name}"}


@app.get("/greet")
def greet_query(name: str) -> dict:
    return {"message": f"How are you doing, {name}"}


@app.get("/regreet/{name}")
def greet_query(name: str, age: int) -> dict:
    return {
        "message": f"How are you doing, {name}. I heard you are {age} years old. Is that true?"
    }


@app.get("/optionalgreet")
async def greet_query(name: Optional[str] = "TheTayo", age: int = 0) -> dict:
    return {
        "message": f"How are you doing, {name}. I heard you are {age} years old. Is that true?"
    }





@app.post("/create_book")
async def create_book(book_data: BookCreateModel) -> dict:
    return {"title": book_data.title, "author": book_data.author}


@app.get("/get_headers", status_code=201)
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
