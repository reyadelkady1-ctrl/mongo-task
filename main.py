from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri)

db = client["students"]
collection = db["people"]

name = input("Enter your name: ")
age = int(input("Enter your age: "))

person = {
    "name": name,
    "age": age
}

collection.insert_one(person)

print("Data saved successfully!")