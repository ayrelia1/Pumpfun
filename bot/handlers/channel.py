
from config import Bot, F, Router, FSInputFile, types, FSMContext, State, bot, CallbackData, FSInputFile, settings
from markups.markup import *
from sql_function import databasework
import datetime
from aiogram.types import Chat
from aiogram.filters import CommandStart
from db.db import async_session
from db.models import Tokens
from check_tokens import get_token_price
import re

router = Router()






@router.channel_post(F.chat.id == settings.CHANNEL_ID)
async def start(message: types.Message):
    text = message.text
    if 'Token' in message.text and 'Profit:' not in message.text:
        # Регулярные выражения для поиска нужных данных
        token_pattern = r'Token:\s*([a-zA-Z0-9]+)'
        mcap_pattern = r'MCap\s*-\s*\$([\d.,]+)'
        name_pattern = r'💊\s*([A-Za-z]+)'
        symbol_pattern = r'\|\s*(#[A-Za-z]+)'
        volume_pattern = r'Volume\s*-\s*\$([\d.,]+)'

        # Поиск данных
        address = re.search(token_pattern, text).group(1)
        mcap = re.search(mcap_pattern, text).group(1)
        name = re.search(name_pattern, text).group(1)
        symbol = re.search(symbol_pattern, text).group(1)
        volume = re.search(volume_pattern, text).group(1)
        
    current_price, mcap, symbol = await get_token_price(address)
    async with async_session() as session:
        token = Tokens(
            address=address,
            name=name,
            symbol=symbol,
            Mcap=float(mcap),
            Volume=float(volume),
            price=str(current_price),
            chat_id=message.chat.id,
            message_id=message.message_id
        )
        session.add(token)
        await session.commit()







channel = router