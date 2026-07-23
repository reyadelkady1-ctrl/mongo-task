from app.database import students_collection


def create_student(student):
    students_collection.insert_one(student.model_dump())
    return {"message": "Student added successfully!"}