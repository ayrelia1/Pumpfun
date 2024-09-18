from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
# from db.db import engine, async_session

from sqlalchemy import BigInteger, Boolean, Date, DateTime, Float, ForeignKey, text, JSON, event, func, ARRAY, NUMERIC
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import Integer, String, CheckConstraint, UniqueConstraint
import asyncio




class Base(AsyncAttrs, DeclarativeBase):
    pass

class Tokens(Base):
    __tablename__ = 'tokens'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)  # Используем Integer для автоинкремента
    address = mapped_column(String(1000), nullable=False)
    name = mapped_column(String(100), nullable=False)
    symbol = mapped_column(String(100), nullable=False)
    Mcap = mapped_column(Float, nullable=False)
    Volume = mapped_column(Float, nullable=False)
    price = mapped_column(String(50), nullable=False)
    max_x = mapped_column(Float, nullable=False, server_default='1')
    chat_id = mapped_column(BigInteger)  # Оставляем BigInteger для других полей, если это необходимо
    message_id = mapped_column(BigInteger)
    
    datetime_parse_token = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


