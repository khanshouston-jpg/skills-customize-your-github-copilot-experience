# 📘 Assignment: Building REST APIs with FastAPI framework

## 🎯 Objective

Build a small REST API using FastAPI that exposes CRUD endpoints for a simple resource (e.g., "items"). Students will define Pydantic models, implement basic in-memory storage, and test the API with `uvicorn` or HTTP requests.

## 📝 Tasks

### 🛠️ Task 1 — Create the API scaffold

#### Description
Create a FastAPI application with a router for an `Item` resource.

#### Requirements
- Implement `GET /items` to list all items
- Implement `GET /items/{item_id}` to return a single item by id
- Implement `POST /items` to add a new item
- Implement `PUT /items/{item_id}` to update an item
- Implement `DELETE /items/{item_id}` to remove an item

### 🛠️ Task 2 — Use Pydantic models and validation

#### Description
Define `Item` and `ItemCreate` Pydantic models to validate input and shape responses.

#### Requirements
- Fields: `id: int`, `name: str`, `description: Optional[str]`, `price: float`
- Validate that `name` is non-empty and `price` is non-negative

### 🛠️ Task 3 — Run and test the API

#### Description
Run the server locally with `uvicorn` and use `curl` or an HTTP client to test the endpoints.

#### Requirements
- Provide example `curl` commands in this README to create and fetch items
- Ensure the server runs on port 8000 by default

## Running locally

1. Install dependencies: `pip install fastapi uvicorn`
2. Run: `uvicorn starter-code:app --reload --port 8000`

## Starter files

- `starter-code.py` — minimal FastAPI scaffold to get started
