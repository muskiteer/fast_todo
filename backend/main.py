from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from internal.database import Base, engine, get_db
from models.todos import todos  # This imports the 'todos' class
from models.user import User
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    password: str

class TodoCreate(BaseModel):
    username: str
    todo: str

# 1. Define the lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
 
    print("Starting up...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Startup complete. Database tables created.")

    yield 

    print("Shutting down...")
    
app = FastAPI(lifespan=lifespan)

@app.post("/todos/")
async def create_todo(todo: TodoCreate, db: AsyncSession = Depends(get_db)):
    new_todo = todos(username=todo.username, todo=todo.todo)
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo


@app.post("/users/")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # In a real application, you should check if username already exists
    # and hash the password before storing
    hashed_password = user.password  # Replace with proper hashing
    
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    # Don't return the hashed password
    return {"id": new_user.id, "username": new_user.username}