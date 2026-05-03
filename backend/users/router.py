
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import SessionLocal
from users import model, schemas
from typing import List
import json
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .model import User as UserModel
from .schemas import User as UserSchema
import jwt
from datetime import datetime, timedelta
import bcrypt

router = APIRouter(prefix="/user", tags=["user"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Инициализация: создать первого администратора, если таблица пуста
@router.post("/init", summary="Инициализация - создать первого администратора")
def create_first_admin(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Создаёт первого пользователя и даёт ему роль 'admin'. Доступно только если в БД ещё нет пользователей."""
    try:
        total = db.query(model.User).count()
        if total > 0:
            raise HTTPException(status_code=400, detail="Пользователи уже существуют")

        if not user.username or not user.password:
            raise HTTPException(status_code=400, detail="Username и пароль обязательны")
        if len(user.password) < 6:
            raise HTTPException(status_code=400, detail="Пароль должен быть от 6 символов")

        hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()

        db_user = model.User(
            username=user.username,
            password=hashed,
            name=user.name,
            group="admin",
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"message": "Admin created", "id": db_user.id, "username": db_user.username}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        print(f"❌ Ошибка при инициализации admin: {e}")
        raise HTTPException(status_code=500, detail=str(e))

####################################################
# 🔐 НАСТРОЙКИ БЕЗОПАСНОСТИ
SECRET_KEY = "your_secret_key"  # ⚠️ Замените на случайную строку в продакшене
ALGORITHM = "HS256"
TOKEN_LIFE_TIME = 60
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

def create_jwt_token(data: dict):
    to_encode = data.copy()
    time = datetime.now() + timedelta(minutes=TOKEN_LIFE_TIME)
    to_encode["lifetime"] = time.timestamp()
    to_encode = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return to_encode

def get_user_from_token(token: str):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if data["lifetime"] < datetime.now().timestamp():
            raise HTTPException(status_code=401, detail="Время жизни токена истекло")
        return data["username"]
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Неверный токен")

# ✅ Зависимость: получение текущего пользователя из БД
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = get_user_from_token(token)
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user

# ✅ Зависимость: проверка роли администратора
def check_admin_role(current_user: UserModel = Depends(get_current_user)):
    # Проверяем поле 'group'. Если там 'admin' - доступ разрешен
    if current_user.group != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Требуемые права доступа: admin"
        )
    return current_user
####################################################

@router.post("/login", summary="вход студента/ логин")
def stud_login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """Вход студента. На вход принимает login и password, возвращает JWT-токен."""
    user = db.query(UserModel).filter(UserModel.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Проверяем хеш пароля
    try:
        if not bcrypt.checkpw(form_data.password.encode(), user.password.encode()):
            raise HTTPException(status_code=404, detail="User not found")
    except ValueError:
        raise HTTPException(status_code=500, detail="Ошибка проверки пароля")
    token = create_jwt_token({"username": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserSchema, summary="информация о текущем студенте")
def get_current_student(current_user: UserModel = Depends(get_current_user)):
    """Возвращает данные пользователя, чей токен был использован."""
    return current_user

# ✅ ТОЛЬКО ДЛЯ АДМИНОВ: Создание нового пользователя
@router.post("/", response_model=schemas.User, summary="Создать пользователя (только admin)")
def create_user(
    user: schemas.UserCreate, 
    db: Session = Depends(get_db), 
    current_user: UserModel = Depends(check_admin_role)  # 🔒 Проверка роли
):
    try:
        if not user.username or not user.password:
            raise HTTPException(status_code=400, detail="Username и пароль обязательны")
        if len(user.password) < 6:
            raise HTTPException(status_code=400, detail="Пароль должен быть от 6 символов")
        
        existing = db.query(model.User).filter(model.User.username == user.username).first()
        if existing:
            raise HTTPException(status_code=400, detail="Username уже занят")
        # Хешируем пароль перед сохранением
        hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()

        db_user = model.User(
            username=user.username,
            password=hashed,
            name=user.name,
        )
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        print(f"❌ Ошибка: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ✅ ТОЛЬКО АВТОРИЗОВАННЫЕ: Получить всех студентов
@router.get("/all_user", response_model=List[schemas.User], summary="Получить всех студентов")
def read_users(
    db: Session = Depends(get_db), 
    current_user: UserModel = Depends(get_current_user)  # 🔒 Просто авторизация
):
    try:
        return db.query(model.User).all()
    except Exception as e:
        print(f"❌ Ошибка загрузки: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(model.User).filter(model.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользовател")
    return db_user
