from fastapi import APIRouter

from app.schemas.borrowing_schema import (
    BorrowBookRequest,
    BorrowBookResponse,
)

from app.schemas.book_schema import StudentBookResponse

from app.services.borrowing_service import (
    borrow_book_service,
    get_student_books_service,
)

router = APIRouter()


@router.post(
    "/borrow",
    response_model=BorrowBookResponse,
)
def borrow_book(
    borrow: BorrowBookRequest,
) -> BorrowBookResponse:
    return borrow_book_service(borrow)


@router.get(
    "/students/{student_id}/books",
    response_model=list[StudentBookResponse],
)
def get_student_books(
    student_id: str,
) -> list[StudentBookResponse]:
    return get_student_books_service(student_id)