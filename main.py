from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

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