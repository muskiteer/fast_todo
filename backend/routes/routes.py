from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.todos import get_todos, insert_todo, update_todo, delete_todo
from models.user import login, register
from internal.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from internal.get_token import get_current_user


todo_router = APIRouter(prefix="/api", tags=["todos"])

class TodoCreate(BaseModel):
    
    todo: str
    done: bool = False

class User(BaseModel):
    username: str
    password: str

@todo_router.post("/users/login")
async def login_routes(user: User, db: AsyncSession = Depends(get_db)):
    return await login(user, db)


@todo_router.post("/users/register")
async def register_routes(user: User, db: AsyncSession = Depends(get_db)):
    return await register(user, db)

@todo_router.get("/users/auth")
async def get_users_routes(username: str = Depends(get_current_user)):
    return {"username": username}

@todo_router.get("/todos/")
async def get_todos_routes(db: AsyncSession = Depends(get_db), username: str = Depends(get_current_user)):
    return await get_todos(db, username)

@todo_router.post("/todos/")
async def create_todo_routes(todo: TodoCreate, db: AsyncSession = Depends(get_db), username: str = Depends(get_current_user)):
    return await insert_todo(todo, db, username)

@todo_router.delete("/todos/{id}")
async def delete_todo_routes(id: int, db: AsyncSession = Depends(get_db), username: str = Depends(get_current_user)):
    return await delete_todo(id, db, username)

@todo_router.put("/todos/{id}")
async def update_todo_routes(id: int, todo: TodoCreate, db: AsyncSession = Depends(get_db), username: str = Depends(get_current_user)):
    return await update_todo(id, todo, db, username)

