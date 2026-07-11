from pymongo import MongoClient

uri = "mongodb+srv://reyad:Reyad132007elkady@cluster0.2x7qdza.mongodb.net/?appName=Cluster0&compressors=zlib"

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