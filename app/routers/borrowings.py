from fastapi import APIRouter

from app.schemas.borrowing import Borrow
from app.services.borrowing_service import (
    borrow_book_service,
    get_student_books_service,
)

router = APIRouter()


@router.post("/borrow")
def borrow_book(borrow: Borrow):
    return borrow_book_service(borrow)


@router.get("/students/{student_id}/books")
def get_student_books(student_id: str):
    return get_student_books_service(student_id)