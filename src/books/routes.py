from fastapi import APIRouter, status, Header, Depends
from fastapi.exceptions import HTTPException
from src.books.service import BookService
from src.books.schemas import Book, BookCreateModel, BookUpdateModel
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession


from typing import List, Optional

book_router = APIRouter()
book_service = BookService()


@book_router.get("/", response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(
    book_data: BookCreateModel, session: AsyncSession = Depends(get_session)
) -> dict:
    new_book = await book_service.create_book(book_data, session)
    return new_book


@book_router.get("/book_uid", response_model=Book)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session)) -> dict:
    the_book = await book_service.get_book(book_uid, session)

    if the_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    else:
        return the_book


@book_router.patch("/book_uid", response_model=Book)
async def update_book(
    book_uid: str,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
) -> dict:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)

    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    else:
        return updated_book


@book_router.delete("/book_uid", status_code=status.HTTP_201_CREATED)
async def delete_book(
    book_uid: str,
    session: AsyncSession = Depends(get_session),
):
    deleted_book = book_service.delete_book(book_uid, session)

    if deleted_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    else:
        return {}
