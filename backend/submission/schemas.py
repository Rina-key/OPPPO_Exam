from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional, Dict, Any
from datetime import datetime
import json


class SubmissionCreate(BaseModel):
    section: str
    answers: Dict[str, Any]

# --- Для ответа (исходящие данные) ---
class SubmissionResponse(BaseModel):
    id: int
    section: str
    data: Dict[str, Any]
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    
    @field_validator('data', mode='before')
    @classmethod
    def parse_data(cls, value):
        """Безопасный парсинг JSON из БД"""
        if value is None or value == "":
            return {}
        if isinstance(value, dict):
            return value
        if isinstance(value, str):
            try:
                return json.loads(value)
            except (json.JSONDecodeError, TypeError, ValueError):
                return {}
        return {}