"""
FastAPI application entry point.
- Includes the todos router
- Creates database tables on startup
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.api.routers.todos import router as todos_router

# Create the database tables (idempotent)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",    # React default
        "http://localhost:5173",    # Vite default
        "http://localhost:4200",    # Angular default
        "http://127.0.0.1:3000",    # Alternative localhost
        "http://127.0.0.1:5173",    # Alternative localhost
        "http://127.0.0.1:4200",    # Alternative localhost
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(todos_router)


@app.get("/health")
def health_check():
    """Simple health-check endpoint."""
    return {"status": "ok"}
