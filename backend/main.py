# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
# from users import router as user_router
# from submission import router as submission_router
# from db import engine, Base, SessionLocal
# from users import model as user_model
# import json
# from fastapi.middleware.cors import CORSMiddleware

# Base.metadata.create_all(bind=engine)
# app = FastAPI(title="diplom")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173",  # Vite
#         "http://127.0.0.1:5173",
#         "http://localhost:3000",  # если используете другой порт
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],  # Разрешаем все методы (GET, POST, PUT, DELETE)
#     allow_headers=["*"],  # Разрешаем все заголовки
# )

# app.include_router(user_router)

# app.include_router(submission_router)


# class User(BaseModel):
#     username: str
#     password: str


# class Submission(BaseModel):
#     section: str
#     answers: dict

# @app.get("/")
# def root():
#     return {"message": "API работает!"}


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware

from users import router as user_router
from submission import router as submission_router
from db import engine, Base, get_db

# создаём таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI(title="diplom")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# роуты
app.include_router(user_router)
app.include_router(submission_router)


@app.get("/")
def root():
    return {"message": "API работает!"}


# 🔥 ГЛАВНЫЙ ENDPOINT ПРОВЕРКИ БД
@app.get("/health/db")
def check_db(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "db_response": result.scalar(),
            "database": str(engine.url),  # покажет куда реально подключились
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )



