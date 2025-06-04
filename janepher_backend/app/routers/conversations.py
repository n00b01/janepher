from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.conversation import Conversation
from app.models.message import Message
from app.schemas.conversation import ConversationCreate, ConversationRead
from app.schemas.message import MessageCreate, MessageRead
from app.auth import get_current_user
from sqlalchemy.sql import func

router = APIRouter(prefix="/conversations", tags=["Conversations"])

@router.post("/", response_model=ConversationRead)
def create_conversation(conversation: ConversationCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    new_convo = Conversation(user_id=current_user.id, title=conversation.title or "Fashion Chat", context=conversation.context)
    db.add(new_convo)
    db.commit()
    db.refresh(new_convo)
    return new_convo

@router.get("/", response_model=List[ConversationRead])
def get_user_conversations(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Conversation).filter(Conversation.user_id == current_user.id).order_by(Conversation.updated_at.desc()).all()

@router.get("/{conversation_id}", response_model=ConversationRead)
def get_conversation(conversation_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    convo = db.query(Conversation).filter(Conversation.id == conversation_id, Conversation.user_id == current_user.id).first()
    if not convo:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return convo

@router.post("/{conversation_id}/messages", response_model=MessageRead)
def create_message(conversation_id: int, message: MessageCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    convo = db.query(Conversation).filter(Conversation.id == conversation_id, Conversation.user_id == current_user.id).first()
    if not convo:
        raise HTTPException(status_code=404, detail="Conversation not found")

    msg = Message(
        conversation_id=conversation_id,
        content=message.content,
        role=message.role,
        has_image=message.has_image,
        image_url=message.image_url,
        fashion_tags=message.fashion_tags
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    convo.updated_at = func.now()
    db.commit()
    return msg
