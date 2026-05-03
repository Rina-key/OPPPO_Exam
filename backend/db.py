from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL  # ← Импортируем URL
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

load_dotenv(encoding="utf-8")



# 🔥 Создаём URL через SQLAlchemy — спецсимволы обрабатываются автоматически!
db_url = URL.create(
    drivername="postgresql",
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),  # ← Не кодируем!
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=int(os.getenv("POSTGRES_PORT", "5432")),
    database=os.getenv("POSTGRES_DB"),
)

# Отладка: показываем URL подключения без специальных символов
print(f"DB URL: {db_url}")

engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass

try:
    # Попытка подключиться к Postgres (Docker)
    conn = engine.connect()
    conn.close()
except Exception:
    # Если подключение не удалось — падаем на SQLite для разработки/тестов
    print("Postgres недоступен, переключаюсь на SQLite (локально)")
    engine = create_engine("sqlite:///./dev.db", connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()