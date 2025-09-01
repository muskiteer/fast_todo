from fastapi import APIRouter
import models.todos

todo_router = APIRouter(prefix="/todos", tags=["todos"])

def not_implemented():
    return {"not implemented"}

@todo_router.get("/")
def login_routes():
    return not_implemented()

    



