from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Базовый класс для всех моделей
class Base(DeclarativeBase):
    pass

# Подключение к SQLite (файл test.db в текущей папке)
engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)