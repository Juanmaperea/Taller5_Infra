from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import student_controller
from app.database import Base, engine

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Students API (Postgres)")

# Keep CORS permissive for now (reverse proxy avoids cross-origin in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(student_controller.router, prefix="/api/students")
