from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.todos import get_todos, insert_todo, update_todo, delete_todo
from models.user import login, logout, register, auth
from internal.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

todo_router = APIRouter(prefix="/api", tags=["todos"])

class TodoCreate(BaseModel):
    username: str
    todo: str

@todo_router.post("/users/login")
def login_routes():
    return login()

@todo_router.post("/users/logout")
def logout_routes():
    return logout()

@todo_router.post("/users/register")
def register_routes():
    return register()

@todo_router.get("/users/auth")
def get_users_routes():
    return auth()

@todo_router.get("/todos/get")
def get_todos_routes():
    return get_todos()

@todo_router.post("/todos/post")
async def create_todo_routes(todo: TodoCreate, db: AsyncSession = Depends(get_db)):
    return await insert_todo(todo, db)

@todo_router.delete("/todos/delete")
async def delete_todo_routes(todo_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_todo(todo_id, db)

@todo_router.put("/todos/update")
def update_todo_routes():
    return update_todo()

