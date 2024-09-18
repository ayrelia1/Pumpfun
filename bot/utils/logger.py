import asyncio
import logging
from logging.handlers import RotatingFileHandler

from config import bot, current_directory, Bot, settings

class TelegramLogsHandler(logging.Handler):
    def __init__(self, bot, chat_id):
        super().__init__()
        self.bot: Bot = bot
        self.chat_id = chat_id

    async def send_message(self, text):
        await self.bot.send_message(chat_id=self.chat_id, text=text[-4096:], message_thread_id=settings.TRACE_BACK_THREAD_ID, parse_mode=None)

    def emit(self, record):
        log_entry = self.format(record)
        try:
            asyncio.create_task(self.send_message(log_entry))
        except:
            pass

log_filename = str((current_directory + "/logs/logs.log"))
logger = logging.getLogger()
logger.setLevel(logging.INFO)
text_format = logging.Formatter("%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s" )

logging.getLogger("apscheduler").setLevel(logging.WARNING)

file_handler = RotatingFileHandler(filename=log_filename, maxBytes=10*1024*1024, backupCount=10, encoding="UTF-8")

file_handler.setLevel(logging.INFO)
file_handler.setFormatter(text_format)

# telegram_handler = TelegramLogsHandler(bot, settings.ADMIN_CHAT_ID)
# telegram_handler.setLevel(logging.ERROR)
# telegram_handler.setFormatter(text_format)


# Создать консольный обработчик
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(text_format)

# Добавить обработчики к логгеру
logger.addHandler(file_handler)
# logger.addHandler(telegram_handler)
logger.addHandler(console_handler)