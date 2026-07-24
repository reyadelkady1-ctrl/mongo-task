from app.database import students_collection
from app.schemas.student_schema import (
    StudentCreateRequest,
    StudentResponse,
)


def create_student(student: StudentCreateRequest) -> StudentResponse:
    result = students_collection.insert_one(student.model_dump())

    return StudentResponse(
        id=str(result.inserted_id),
        name=student.name,
        age=student.age,
    )