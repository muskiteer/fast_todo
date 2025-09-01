from sqlalchemy import Boolean, Column, Integer, String
from internal.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

def login():
    return {"login"}

def logout():
    return {"logout"}

def register():
    return {"register"}

def auth():
    return {"auth"}
