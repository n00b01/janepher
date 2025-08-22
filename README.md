# Janepher Backend

Backend API for **Janepher**, a fashion AI web app built with FastAPI and PostgreSQL.

## Features
- FastAPI REST API
- PostgreSQL + SQLAlchemy + Alembic
- JWT Authentication
- CRUD: Users, Conversations, Messages
- Swagger Docs at `/docs`

## Tech Stack
FastAPI, PostgreSQL, Pydantic, Alembic, Uvicorn

## Getting Started

```bash
# Activate environment
.\.venv\Scriptsactivate

# Run server
uvicorn main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

## DB Setup

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/janepher
```

```bash
alembic upgrade head
```

## credits 🎉

 **Greg Enos**

[https://github.com/n00b01](https://github.com/n00b01)

 **Mark Ndwaru** 
 
[https://github.com/Marcos-dev41](https://github.com/Marcos-dev41)
