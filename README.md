# Ticket API

A simple FastAPI application providing endpoints for managing tickets and batches.

## Requirements

- Python 3.10+
- [Poetry](https://python-poetry.org/) for dependency management

## Running locally

```bash
# Install dependencies
poetry install

# Run database migrations
poetry run alembic upgrade head

# Start the API
poetry run uvicorn ticket_api.main:app --reload
```

The API will be available at `http://localhost:8000`.
