from operator import sub
from sqlalchemy import Boolean, Column, Integer, String
from internal.database import Base
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from internal.jwt import get_password_hash, verify_password, create_access_token, decode_access_token
from fastapi import HTTPException, status



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

async def login(user_data, db: AsyncSession):
    result = await db.execute(select(User).where(User.username == user_data.username))
    user = result.scalar()
    if not user or not verify_password(user_data.password, user.hashed_password):
        return {"error": "invalid credentials"}
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer", "id": user.id, "username": user.username}


async def register(user_data, db: AsyncSession):
    result = await db.execute(select(User).where(User.username == user_data.username))
    existing_user = result.scalar()
    if existing_user:
        return {"error": "user already exists"}
    hashed_password = get_password_hash(user_data.password)
    new_user = User(username=user_data.username, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {"id": new_user.id, "username": new_user.username}


