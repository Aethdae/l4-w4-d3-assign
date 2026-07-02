import os
from flask import Flask, request
from flask_cors import CORS
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app, origins=["http://localhost:*", "http://127.0.0.1:*"])

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

@app.route("/")
def home():
    return {"message": "Healthy"}

@app.get("/api/users")
def users():
    response = supabase.from_("users").select("*").execute()
    return {"users": response.data, "count": response.count}

@app.post("/api/users/add")
def add_user():
    if request.json:
        user = request.json
        if not user.get("name") or not user.get("email"):
            return {"error": "Incorrect user format."}, 415
        
        response = supabase.from_("users").insert(user).execute()
        return {"message": "User added", "created": response.data}, 201
    return {"error":"Json expected."}

if __name__ == "__main__":
    app.run()