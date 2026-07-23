from fastapi import APIRouter

from app.schemas.student import Student
from app.services.student_service import create_student

router = APIRouter()


@router.post("/students")
def add_student(student: Student):
    return create_student(student)