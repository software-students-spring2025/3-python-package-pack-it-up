from pymongo import MongoClient
import random
import certifi
import os

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(
    "mongodb+srv://sms10010:Password@cluster0.jrofj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsCAFile=certifi.where())
db = client["lazyCommit"]
commit_collection = db["commitMessages"]
excusesDB = db["excuses"]
hakiuDB = db["haikus"]


def random_commit_message():
    messages = list(db.commitMessages.find())
    if messages:
        all_messages = [msg for doc in messages for msg in doc["messages"]]
        return random.choice(all_messages) if all_messages else "No commit messages found!"
    return "No commit messages found!"


def generate_commit_message(style: str):
    messages = list(db.commitMessages.find({"style": style}))
    if messages:
        all_messages = [msg for doc in messages for msg in doc["messages"]]
        return random.choice(all_messages) if all_messages else f"No commit messages found for style: {style}"
    return f"No commit messages found for style: {style}"


def git_blame_excuse():
    excuses_data = list(db.excuses.find())
    if excuses_data:
        excuses = excuses_data[0].get("excuses", [])
        if excuses:
            return random.choice(excuses)
    return "No excuses found!"


def generate_haiku():
    haikus = list(db.haikus.find())
    if haikus:
        haiku = haikus[0].get("haikus", [])
        if haiku:
            return random.choice(haiku)
    return "No haikus found!"


def add_commit_message(style: str, message: str):
    if not message:
        return "No message provided!"
    existing_style = commit_collection.find_one({"style": style})

    if existing_style:
        result = commit_collection.update_one(
            {"style": style},
            {"$push": {"messages": message}}
        )

        if result.modified_count > 0:
            return f"Message added successfully to the '{style}' style."
        else:
            return f"Message already exists in the '{style}' style."
    else:
        new_commit = {
            "style": style,
            "messages": [message]
        }

        result = commit_collection.insert_one(new_commit)

        if result.inserted_id:
            return f"New style '{style}' created and message added successfully."
        else:
            return "Failed to add message."
