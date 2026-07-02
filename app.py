from flask import Flask, request
from flask_cors import CORS
from sqlalchemy import select
from sqlalchemy.orm import Session
from models import User
from db import engine

app = Flask(__name__)
CORS(app, origins=["http://localhost:*", "http://127.0.0.1:*"])

@app.get("/")
def home():
    return {"message": "Healthy"}

@app.get("/routes")
def routes():
    return { "message": {
        "Home/Health Check": "/", 
        "GET users": "/api/users", 
        "POST add_user {'name': string, 'email': string}": "/api/users/add", 
        "routes": "/routes"
    }}

@app.get("/api/users")
def get_users():
    with Session(engine) as session:
        users = session.scalars(select(User)).all()

        return {
            "users": [user.to_dict() for user in users],
            "count": len(users)
        }

    
@app.post("/api/users/add")
def add_user():
    data = request.json
    if not data.get("name") or not data.get("email"):
        return {"error": "name and email are required fields"}, 415
    
    user = User(data)
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)

    return {
        "resource": user.to_dict(),
        "message": "Success",
    }, 201

if __name__ == "__main__":
    app.run()