# Todo API (FastAPI + SQLite)

Backend simple que implementa un CRUD completo para un sistema de "todo" usando FastAPI y SQLite.

## Estructura del proyecto

```
app/
├─ api/
│  └─ routers/
│     └─ todos.py        # Endpoints REST de Todo
├─ core/
│  └─ database.py        # Configuración de SQLAlchemy/SQLite y sesión
├─ models/
│  └─ todo.py            # Modelo ORM de SQLAlchemy
├─ schemas/
│  └─ todo.py            # Modelos Pydantic (entrada/salida)
├─ services/
│  └─ todo_service.py    # Lógica de negocio CRUD
└─ main.py               # App FastAPI y registro de routers
```

Cada archivo y función incluye comentarios breves explicando su función.

## Requisitos

- Python 3.11+
- Dependencias en `requirements.txt` (FastAPI, Uvicorn, SQLAlchemy, Pydantic)

Instalación de dependencias (recomendado dentro de un entorno virtual):

```
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Ejecutar la aplicación

Genera y usa una base de datos SQLite local (`todos.db` en la raíz).

```
uvicorn app.main:app --reload
```

- Documentación interactiva (Swagger UI): http://127.0.0.1:8000/docs
- Alternativa Redoc: http://127.0.0.1:8000/redoc
- Health check: http://127.0.0.1:8000/health

## Endpoints principales

Base path: `/todos`

- POST `/todos/` — Crear tarea
- GET `/todos/` — Listar todas
- GET `/todos/{id}` — Obtener una
- PUT `/todos/{id}` — Actualizar
- DELETE `/todos/{id}` — Eliminar

## Ejemplos con curl

Crear una tarea:

```
curl -X POST http://127.0.0.1:8000/todos/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Comprar pan",
    "description": "Ir a la panadería a las 6pm",
    "completed": false
  }'
```

Listar todas:

```
curl http://127.0.0.1:8000/todos/
```

Obtener por id (ej. 1):

```
curl http://127.0.0.1:8000/todos/1
```

Actualizar (ej. 1):

```
curl -X PUT http://127.0.0.1:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Comprar pan integral",
    "completed": true
  }'
```

Eliminar (ej. 1):

```
curl -X DELETE http://127.0.0.1:8000/todos/1 -i
```

Manejo de errores: si se intenta acceder/actualizar/eliminar una tarea que no existe, la API responde con HTTP 404 y un mensaje `{"detail": "Todo no encontrado"}`.

## Notas

- Las tablas se crean automáticamente al iniciar la app.
- El servicio usa SQLAlchemy en modo síncrono para simplicidad.
- Los modelos Pydantic validan entrada y salida (con `from_attributes=True` para mapear desde ORM).
