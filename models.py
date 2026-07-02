from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    def __init__(self, data):
        self.name = data.get("name")
        self.email = data.get("email")

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, ID: {self.id}"
    
    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "email": self.email
            }