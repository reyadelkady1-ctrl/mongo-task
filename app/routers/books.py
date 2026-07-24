from fastapi import APIRouter

from app.schemas.book_schema import (
    BookCreateRequest,
    BookResponse,
)
from app.services.book_service import create_book

router = APIRouter()


@router.post("/books", response_model=BookResponse)
def add_book(book: BookCreateRequest) -> BookResponse:
    return create_book(book)