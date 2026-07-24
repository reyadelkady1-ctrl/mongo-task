from pydantic import BaseModel


class BorrowBookRequest(BaseModel):
    student_id: str
    book_id: str


class BorrowBookResponse(BaseModel):
    message: str