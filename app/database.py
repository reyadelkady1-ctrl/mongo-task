import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri)

db = client["library"]

students_collection = db["students"]
books_collection = db["books"]
borrowings_collection = db["borrowings"]