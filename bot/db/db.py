from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
import os

# Используем SQLite как базу данных
sqlalchemy_url = f"sqlite+aiosqlite:///{os.environ.get('DB_NAME')}.db"

engine = create_async_engine(
    sqlalchemy_url,
    echo=False,  # Логирование SQL-запросов
    connect_args={"timeout": 60},  # Устанавливаем таймаут подключения в 60 секунд
    pool_pre_ping=True,  # Проверка соединений (хотя для SQLite это не всегда критично)
)

# Создаем асинхронную сессию
async_session = async_sessionmaker(engine)