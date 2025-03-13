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
    # print(f"DEBUG: Messages for style '{style}':", messages)
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

