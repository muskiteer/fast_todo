from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from internal.database import Base, engine, get_db
from pydantic import BaseModel, EmailStr
from routes.routes import todo_router
from fastapi.middleware.cors import CORSMiddleware


class UserCreate(BaseModel):
    username: str
    password: str

class TodoCreate(BaseModel):
    username: str
    todo: str

@asynccontextmanager
async def lifespan(app: FastAPI):
 
    print("Starting up...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Startup complete. Database tables created.")

    yield 

    print("Shutting down...")
    
app = FastAPI(lifespan=lifespan)

app.include_router(todo_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Or your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

