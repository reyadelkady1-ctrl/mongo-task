from app.database import books_collection


def create_book(book):
    books_collection.insert_one(book.model_dump())
    return {"message": "Book added successfully!"}