from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, select
from internal.database import Base
from sqlalchemy.ext.asyncio import AsyncSession


class todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Fix: make ForeignKey part of the column type definition
    username = Column(String, ForeignKey("users.username"), index=True)
    
    todo = Column(String, index=True)
    done = Column(Boolean, default=False)

async def insert_todo(todo_data, db: AsyncSession):
    new_todo = todos(
        username=todo_data.username, 
        todo=todo_data.todo
    )
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo

def update_todo():
    return {"update_todo"}

async def delete_todo(todo_id, db: AsyncSession):
    db_query = await db.execute(
        select(todos).where(todos.id == todo_id )
    )
    result = db_query.scalar()
    if result:
        await db.delete(result)
        await db.commit()
        return {"successfully deleted": todo_id}

def get_todos():
    return {"get_todos"}


