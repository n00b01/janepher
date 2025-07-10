from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    style_preferences: Optional[str] = None
    size_profile: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime
    style_preferences: Optional[str] = None
    size_profile: Optional[str] = None

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
