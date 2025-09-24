"""
Pydantic models (schemas) for request validation and response serialization.
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    """Shared properties for Todo schemas."""
    title: str = Field(..., min_length=1, max_length=255, description="Short title of the task")
    description: Optional[str] = Field(None, max_length=1024, description="Detailed description")
    completed: bool = Field(default=False, description="Completion status")


class TodoCreate(TodoBase):
    """Schema for creating a new Todo. Inherits required fields from TodoBase."""
    pass


class TodoUpdate(BaseModel):
    """Schema for updating an existing Todo. All fields are optional."""
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1024)
    completed: Optional[bool] = None


class TodoOut(TodoBase):
    """Schema for reading a Todo item in responses."""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # enables ORM mode for SQLAlchemy models
