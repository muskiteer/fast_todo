from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from internal.database import Base

class todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Fix: make ForeignKey part of the column type definition
    username = Column(String, ForeignKey("users.username"), index=True)
    
    todo = Column(String, index=True)
    done = Column(Boolean, default=False)