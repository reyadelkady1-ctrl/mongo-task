from app.database import books_collection
from app.schemas.book_schema import (
    BookCreateRequest,
    BookResponse,
)


def create_book(book: BookCreateRequest) -> BookResponse:
    result = books_collection.insert_one(book.model_dump())

    return BookResponse(
        id=str(result.inserted_id),
        title=book.title,
        author=book.author,
    )