from pydantic import BaseModel


class StudentCreateRequest(BaseModel):
    name: str
    age: int


class StudentResponse(BaseModel):
    id: str
    name: str
    age: int