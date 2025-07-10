from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, conversations
from app.database import engine
from app.models import user, conversation, message  # Fixed import

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
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # More specific origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(conversations.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to Janepher - Your AI Fashion Assistant! 👗✨"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "janepher-backend"}