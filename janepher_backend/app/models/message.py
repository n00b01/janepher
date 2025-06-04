from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=False)
    content = Column(Text, nullable=False)
    role = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    has_image = Column(Boolean, default=False)
    image_url = Column(String, nullable=True)
    fashion_tags = Column(String, nullable=True)
    
    conversation = relationship("Conversation", back_populates="messages")
