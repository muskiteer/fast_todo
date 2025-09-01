from fastapi import APIRouter
from models.todos import get_todos, insert_todo, update_todo, delete_todo
from models.user import login, logout, register, auth

todo_router = APIRouter(prefix="/api", tags=["todos"])

def not_implemented():
    return {"not implemented"}

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
def create_todo_routes():
    return insert_todo()

@todo_router.delete("/todos/delete")
def delete_todo_routes():
    return delete_todo()

@todo_router.put("/todos/update")
def update_todo_routes():
    return update_todo()

