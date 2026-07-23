from fastapi import FastAPI

from app.routers.students import router as student_router
from app.routers.books import router as book_router
from app.routers.borrowings import router as borrowing_router

app = FastAPI()

app.include_router(student_router)
app.include_router(book_router)
app.include_router(borrowing_router)