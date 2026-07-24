from pydantic import BaseModel


class BookCreateRequest(BaseModel):
    title: str
    author: str


class BookResponse(BaseModel):
    id: str
    title: str
    author: str


class StudentBookResponse(BaseModel):
    id: str
    title: str
    author: str