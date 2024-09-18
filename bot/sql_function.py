from typing import Dict, List, Optional, Tuple

import pytz
from config import types
from db.db import async_session, engine
import sys, asyncio
from sqlalchemy import and_, or_, text, bindparam
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.future import select

import json
import datetime
from sqlalchemy.ext.asyncio import AsyncSession

class databasework:
    
    
    

    async def get_all_tokens():
        month_date = datetime.datetime.now() - datetime.timedelta(days=30)
        async with async_session() as session:
            async with session.begin():
                sql = "SELECT * FROM tokens WHERE datetime_parse_token > :month_date"
                result = await session.execute(text(sql), {"month_date": month_date})
            return result.all()  # Возвращает все строки

    async def update_max_notified_multiplier_token(max_notified_multiplier: int, id: int):
        async with async_session() as session:
            async with session.begin():
                sql = "UPDATE tokens SET max_x = :max_x WHERE id = :id"
                await session.execute(text(sql), {"max_x": max_notified_multiplier, "id": id})
            await session.commit()
    
    
    async def create_user(user_id: int, username: str):
        async with async_session() as session:
            async with session.begin():
                sql = """
                INSERT INTO users (user_id, username)
                VALUES (:user_id, :username)
                """
                await session.execute(text(sql), {"user_id": user_id, "username": username})
            await session.commit()  # Подтверждение транзакции
    
