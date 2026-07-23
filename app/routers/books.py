from fastapi import APIRouter

from app.schemas.book import Book
from app.services.book_service import create_book

router = APIRouter()


@router.post("/books")
def add_book(book: Book):
    return create_book(book)