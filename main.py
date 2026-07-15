from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import os

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri)

db = client["library"]

students_collection = db["students"]
books_collection = db["books"]
borrowings_collection = db["borrowings"]

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int


class Book(BaseModel):
    title: str
    author: str


class Borrow(BaseModel):
    student_id: str
    book_id: str


@app.post("/students")
def add_student(student: Student):
    students_collection.insert_one(student.model_dump())
    return {"message": "Student added successfully!"}


@app.post("/books")
def add_book(book: Book):
    books_collection.insert_one(book.model_dump())
    return {"message": "Book added successfully!"}


@app.post("/borrow")
def borrow_book(borrow: Borrow):
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


@app.get("/students/{student_id}/books")
def get_student_books(student_id: str):
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

@app.get("/students/{student_id}/books")
def get_student_books(student_id: str):
    borrowings = borrowings_collection.find({
        "student_id": ObjectId(student_id)
    })

    books = []

    for borrowing in borrowings:
        book = books_collection.find_one({
            "_id": borrowing["book_id"]
        })

        if book:
            books.append({
                "id": str(book["_id"]),
                "title": book["title"],
                "author": book["author"]
            })

    return books