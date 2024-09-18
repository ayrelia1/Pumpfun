from config import dp, logging, bot, Bot, current_directory, root_path
from aiogram.types import BotCommand, BotCommandScopeDefault

from handlers import routers
import asyncio
from db.create_tables import create_tables
from db.db import engine
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import sys
from utils.logger import logger
import gc
from check_tokens import check_price_token

schedulers = AsyncIOScheduler(timezone='Europe/Moscow')



@dp.startup()
async def start_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='🔄 Главное меню'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

    
    schedulers.add_job(check_price_token, 'interval', seconds=10)

    schedulers.start()
    
    logging.error(f"BOT STARTED")

    
    task1 = asyncio.create_task(create_tables()) # создаем базу юзеров если нет

    
@dp.shutdown()
async def dispose(bot: Bot):
    schedulers.shutdown()
    await engine.dispose()
        
                

async def main() -> None:     # функция запуска бота
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s" 
                        ) # логирование
    


    
    #for router in routers:
    dp.include_router(routers) # импорт роутеров
        
        
    try:
        await dp.start_polling(bot) # запуск поллинга
    except Exception as ex:
        print(ex)

        
    
if __name__ == "__main__":
                
    asyncio.run(main()) 