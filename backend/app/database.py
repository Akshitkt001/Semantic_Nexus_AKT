from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
import os

# Use environment variable for MongoDB connection string (better for security)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["semantic_nexus"]

def get_user_data(user_id: str):
    try:
        # Retrieve user preferences from the database
        user = db["users"].find_one({"user_id": user_id})
        return user if user else {}
    except ConnectionFailure:
        print("Error connecting to MongoDB")
        return {}
    except OperationFailure as e:
        print(f"Database operation failed: {e}")
        return {}

def save_user_query(user_id: str, query: str):
    try:
        # Save user's query for personalization
        result = db["queries"].insert_one({"user_id": user_id, "query": query})
        return result.inserted_id
    except ConnectionFailure:
        print("Error connecting to MongoDB")
        return None
    except OperationFailure as e:
        print(f"Database operation failed: {e}")
        return None
