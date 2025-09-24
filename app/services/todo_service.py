"""
Service layer encapsulating business logic for Todo operations.
Separating this logic makes routers thinner and easier to test.
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


def list_todos(db: Session) -> List[Todo]:
    """Return all todos."""
    return db.query(Todo).order_by(Todo.created_at.desc()).all()


def get_todo(db: Session, todo_id: int) -> Todo:
    """Return a single todo by ID or raise 404 if not found."""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo no encontrado")
    return todo


def create_todo(db: Session, payload: TodoCreate) -> Todo:
    """Create and persist a new todo from the provided payload."""
    todo = Todo(
        title=payload.title,
        description=payload.description,
        completed=payload.completed,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update_todo(db: Session, todo_id: int, payload: TodoUpdate) -> Todo:
    """Update fields of an existing todo; raise 404 if the todo doesn't exist."""
    todo = get_todo(db, todo_id)

    if payload.title is not None:
        todo.title = payload.title
    if payload.description is not None:
        todo.description = payload.description
    if payload.completed is not None:
        todo.completed = payload.completed

    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo_id: int) -> None:
    """Delete an existing todo; raise 404 if it doesn't exist."""
    todo = get_todo(db, todo_id)
    db.delete(todo)
    db.commit()
    return None
