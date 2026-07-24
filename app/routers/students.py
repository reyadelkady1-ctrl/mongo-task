from fastapi import APIRouter
from app.services.student_service import create_student

from app.schemas.student_schema import (
    StudentCreateRequest,
    StudentResponse,
)
router = APIRouter()


@router.post("/students")
def add_student(student: StudentCreateRequest) -> StudentResponse:
    return create_student(student)