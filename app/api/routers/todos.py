"""
FastAPI router exposing CRUD endpoints for Todo items.
"""
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.todo import TodoCreate, TodoUpdate, TodoOut
from app.services.todo_service import (
    list_todos,
    get_todo,
    create_todo,
    update_todo,
    delete_todo,
)

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=TodoOut, status_code=status.HTTP_201_CREATED)
def create_todo_endpoint(payload: TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo item."""
    return create_todo(db, payload)


@router.get("/", response_model=List[TodoOut])
def list_todos_endpoint(db: Session = Depends(get_db)):
    """Return all todo items."""
    return list_todos(db)


@router.get("/{todo_id}", response_model=TodoOut)
def get_todo_endpoint(todo_id: int, db: Session = Depends(get_db)):
    """Return a single todo by id."""
    return get_todo(db, todo_id)


@router.put("/{todo_id}", response_model=TodoOut)
def update_todo_endpoint(todo_id: int, payload: TodoUpdate, db: Session = Depends(get_db)):
    """Update a todo by id."""
    return update_todo(db, todo_id, payload)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_endpoint(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo by id. Returns 204 if successful."""
    delete_todo(db, todo_id)
    return None
