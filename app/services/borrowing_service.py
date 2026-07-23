from bson import ObjectId

from app.database import (
    students_collection,
    books_collection,
    borrowings_collection,
)


def borrow_book_service(borrow):

    student = students_collection.find_one(
        {"_id": ObjectId(borrow.student_id)}
    )

    if not student:
        return {"message": "Student not found"}

    book = books_collection.find_one(
        {"_id": ObjectId(borrow.book_id)}
    )

    if not book:
        return {"message": "Book not found"}

    taken = borrowings_collection.find_one(
        {"book_id": ObjectId(borrow.book_id)}
    )

    if taken:
        return {"message": "Book already taken"}

    borrowings_collection.insert_one({
        "student_id": ObjectId(borrow.student_id),
        "book_id": ObjectId(borrow.book_id)
    })

    return {"message": "Book borrowed successfully"}
def get_student_books_service(student_id):

    books = []

    borrowings = borrowings_collection.find(
        {"student_id": ObjectId(student_id)}
    )

    for borrowing in borrowings:

        book = books_collection.find_one(
            {"_id": borrowing["book_id"]}
        )

        if book:

            books.append({
                "id": str(book["_id"]),
                "title": book["title"],
                "author": book["author"]
            })

    return books