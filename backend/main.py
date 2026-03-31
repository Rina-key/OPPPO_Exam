from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from users import router as user_router
from submission import router as submission_router
from db import engine, Base, SessionLocal
from users import model as user_model
import json
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI(title="diplom")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite
        "http://127.0.0.1:5173",
        "http://localhost:3000",  # если используете другой порт
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Разрешаем все заголовки
)

app.include_router(user_router)

app.include_router(submission_router)


class User(BaseModel):
    username: str
    password: str


class Submission(BaseModel):
    section: str
    answers: dict

@app.get("/")
def root():
    return {"message": "API работает!"}






