from pydantic import BaseModel


class Borrow(BaseModel):
    student_id: str
    book_id: str