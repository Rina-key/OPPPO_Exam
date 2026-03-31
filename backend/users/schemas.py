from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional, Dict, Any
from datetime import datetime
import json

class UserCreate(BaseModel):
    username: str
    password: str
    name: Optional[str] = None
    
class User(UserCreate): 
    id: int
    group:  Optional[str] = None
    phone:  Optional[str] = None
    email:  Optional[str] = None
    birth:  Optional[str] = None
    education:  Optional[str] = None
    vk:  Optional[str] = None
    tg:  Optional[str] = None
    model_config = {"from_attributes": True}
   
