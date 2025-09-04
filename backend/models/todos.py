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

async def insert_todo(todo_data, db: AsyncSession , username: str):
    new_todo = todos(
        username=username, 
        todo=todo_data.todo
    )
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo

async def update_todo( id: int, todo_data, db: AsyncSession, username: str):
    db_query = await db.execute(
        select(todos).where(todos.id == id, todos.username == username)
    )
    result = db_query.scalar()
    if result:
        result.todo = todo_data.todo
        result.done = todo_data.done
        await db.commit()
        await db.refresh(result)
        return result
    return {"error": "Todo not found"}

async def delete_todo(id: int, db: AsyncSession, username: str):
    db_query = await db.execute(
        select(todos).where(todos.id == id, todos.username == username)
    )
    result = db_query.scalar()
    if result:
        await db.delete(result)
        await db.commit()
        return {"successfully deleted": result.todo}

async def get_todos(db: AsyncSession, username: str):
    db_query = await db.execute(
        select(todos).where(todos.username == username)
    )
    return db_query.scalars().all()

