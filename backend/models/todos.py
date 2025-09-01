from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from internal.database import Base

class todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Fix: make ForeignKey part of the column type definition
    username = Column(String, ForeignKey("users.username"), index=True)
    
    todo = Column(String, index=True)
    done = Column(Boolean, default=False)


def insert_todo():
    return {"insert_todo"}

def update_todo():
    return {"update_todo"}

def delete_todo():
    return {"delete_todo"}

def get_todos():
    return {"get_todos"}


