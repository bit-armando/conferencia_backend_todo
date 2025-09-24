"""
FastAPI application entry point.
- Includes the todos router
- Creates database tables on startup
"""
from fastapi import FastAPI

from app.core.database import Base, engine
from app.api.routers.todos import router as todos_router

# Create the database tables (idempotent)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API", version="1.0.0")

# Include routers
app.include_router(todos_router)


@app.get("/health")
def health_check():
    """Simple health-check endpoint."""
    return {"status": "ok"}
