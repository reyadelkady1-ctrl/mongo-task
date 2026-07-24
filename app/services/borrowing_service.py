from bson import ObjectId

from app.database import (
    students_collection,
    books_collection,
    borrowings_collection,
)

from app.schemas.borrowing_schema import (
    BorrowBookRequest,
    BorrowBookResponse,
)

from app.schemas.book_schema import StudentBookResponse


def borrow_book_service(
    borrow: BorrowBookRequest,
) -> BorrowBookResponse:

    student = students_collection.find_one(
        {"_id": ObjectId(borrow.student_id)}
    )

    if not student:
        return BorrowBookResponse(
            message="Student not found"
        )

    book = books_collection.find_one(
        {"_id": ObjectId(borrow.book_id)}
    )

    if not book:
        return BorrowBookResponse(
            message="Book not found"
        )

    taken = borrowings_collection.find_one(
        {"book_id": ObjectId(borrow.book_id)}
    )

    if taken:
        return BorrowBookResponse(
            message="Book already taken"
        )

    borrowings_collection.insert_one(
        {
            "student_id": ObjectId(borrow.student_id),
            "book_id": ObjectId(borrow.book_id),
        }
    )

    return BorrowBookResponse(
        message="Book borrowed successfully"
    )


def get_student_books_service(
    student_id: str,
) -> list[StudentBookResponse]:

    books = []

    borrowings = borrowings_collection.find(
        {"student_id": ObjectId(student_id)}
    )

    for borrowing in borrowings:

        book = books_collection.find_one(
            {"_id": borrowing["book_id"]}
        )

        if book:
            books.append(
                StudentBookResponse(
                    id=str(book["_id"]),
                    title=book["title"],
                    author=book["author"],
                )
            )

    return books