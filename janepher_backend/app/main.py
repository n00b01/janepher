from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, conversations
from app.database import engine
from app.models import user, conversation, message

# Create tables
user.Base.metadata.create_all(bind=engine)
conversation.Base.metadata.create_all(bind=engine)
message.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Janepher API",
    description="AI-powered fashion chatbot backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(conversations.router)

@app.get("/")
def root():
    return {"message": "Welcome to Janepher - Your AI Fashion Assistant! 👗✨"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "janepher-backend"}
