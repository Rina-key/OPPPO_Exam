import pytest
from fastapi.testclient import TestClient
from main import app  
client = TestClient(app)


def test_login_success():
    """Успешный вход"""
    response = client.post(
        "/user/login",
        data={"username": "admin", "password": "admin1"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_fail():
    """Неверный логин"""
    response = client.post(
        "/user/login",
        data={"username": "wrong", "password": "wrong"}
    )
    assert response.status_code == 404



def test_submit_success():
    """Успешная отправка теста"""
    payload = {
        "section": "math",
        "answers": {"q1": "A", "q2": "B"}
    }

    response = client.post("/test/submit", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["section"] == "math"
    assert "id" in data


def test_submit_invalid_data():
    """Ошибка при некорректных данных"""
    payload = {
        "section": "math",
        "answers": "INVALID"  # должно быть dict
    }

    response = client.post("/test/submit", json=payload)
    
    assert response.status_code in (422, 500)



def test_get_submissions():
    """Получение списка отправок"""
    response = client.get("/test/submissions")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_submission_not_found():
    """Получение несуществующей отправки"""
    response = client.get("/test/submissions/999999")
    
    assert response.status_code == 404