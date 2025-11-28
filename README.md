# Notes API

Lightweight FastAPI-based Notes API — a minimal example project that demonstrates a simple in-memory CRUD service for notes.

<!-- Badges -->
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](#)

## What this project does

This repository implements a small RESTful API for managing notes. It's built with FastAPI and keeps data in memory (no database). It is intended as a learning or starter project for building APIs, experimenting with FastAPI features, or as a template for small demos.

Key capabilities:
- Create, read, update, and delete notes (CRUD)
- Simple Pydantic schema validation for note objects
- JSON responses and conventional HTTP status codes

## Why this is useful

- Great for learning FastAPI, Pydantic, and building simple microservices.
- Minimal surface area — no DB setup required — ideal for demos and tests.
- Clear structure to extend with persistence, authentication, or async I/O.

## Tech stack

- Python 3.10+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic for schema validation

## Project layout (relevant files)

- `main.py` — application entrypoint and uvicorn runner
- `routers/notes.py` — API routes and route handlers
- `schemas/note.py` — Pydantic model for Note
- `data.py` — simple in-memory data store

## Note schema

The Note model (in `schemas/note.py`) uses Pydantic and includes:

- `note_id` (int)
- `content` (str)
- `createdAt` (string timestamp generated at creation)

## Getting started

Prerequisites: Python 3.10 or newer.

1. Create and activate a virtual environment

```bash
python -m venv .venv
# On Windows (Bash):
source .venv/Scripts/activate
```

2. Install dependencies

There is no `requirements.txt` in this project. Install the minimal dependencies directly:

```bash
pip install fastapi uvicorn pydantic
```

3. Run the API locally

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

You can also run `python main.py` which invokes `uvicorn.run(...)` when executed directly.

## API endpoints

Base prefix: `/api`

- POST `/api/notes` — create a new note
- GET `/api/notes` — list all notes
- GET `/api/notes/{note_id}` — retrieve a specific note by id
- PUT `/api/notes/{note_id}` — update a note's `content`
- DELETE `/api/notes/{note_id}` — delete a note

Example request payload for creating a note:

```json
{
  "note_id": 0,
  "content": "Buy groceries"
}
```

Example curl (create):

```bash
curl -X POST "http://127.0.0.1:8000/api/notes" \
  -H "Content-Type: application/json" \
  -d '{"note_id": 0, "content": "Hello world"}'
```

Fetch all notes:

```bash
curl http://127.0.0.1:8000/api/notes
```

Update a note (PUT):

```bash
curl -X PUT "http://127.0.0.1:8000/api/notes/0" \
  -H "Content-Type: application/json" \
  -d '{"note_id": 0, "content": "Updated content"}'
```

## Development notes and caveats

- Data is stored in memory (`data.py`) and will be lost when the process stops.
- `note_id` is assigned by the application when creating a note — the implementation appends notes and uses the last note's id + 1. Deleted IDs are not reused.
- This project is synchronous; converting to async or adding a database are natural next steps.

## Where to get help

- Open issues on the repository to report bugs or request features.
- Inspect the code in `routers/notes.py` and `schemas/note.py` for implementation details.

## Contributing

Short contribution guidance is in `CONTRIBUTING.md` — please read it before submitting code or issues.

If you want to extend the project, consider:
- Adding persistent storage (SQLite, Postgres)
- Adding tests (pytest) and CI
- Adding request validation and improved error handling

## Maintainers

- Repository owner: `Dev-Prajapati25`

## License

No `LICENSE` file is present in this repository. Add a `LICENSE` file to declare usage terms if you plan to publish or share widely.

---

If you'd like, I can add a minimal `CONTRIBUTING.md` and a `requirements.txt` next. Want me to add those now?
