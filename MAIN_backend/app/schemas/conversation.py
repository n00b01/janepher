from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from .message import MessageRead

class ConversationCreate(BaseModel):
    title: Optional[str] = None
    context: Optional[str] = None

class ConversationRead(BaseModel):
    id: int
    user_id: int
    title: Optional[str]
    context: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    messages: List[MessageRead] = []

    class Config:
        from_attributes = True
