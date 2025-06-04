from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MessageCreate(BaseModel):
    content: str
    role: str
    has_image: Optional[bool] = False
    image_url: Optional[str] = None
    fashion_tags: Optional[str] = None

class MessageRead(BaseModel):
    id: int
    conversation_id: int
    content: str
    role: str
    timestamp: datetime
    has_image: bool
    image_url: Optional[str]
    fashion_tags: Optional[str]

    class Config:
        from_attributes = True
