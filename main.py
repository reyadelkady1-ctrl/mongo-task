from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri)

db = client["students"]
collection = db["people"]

app = FastAPI()


class Person(BaseModel):
    name: str
    age: int


@app.post("/people")
def create_person(person: Person):
    collection.insert_one(person.model_dump())
    return {"message": "Data saved successfully!"}