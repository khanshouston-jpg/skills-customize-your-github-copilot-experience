# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a simple REST API using the FastAPI framework to understand HTTP methods, request/response handling, routing, and basic data validation.

## ⚙️ Prerequisites

- Python 3.8+ programming skills (functions, classes, dictionaries)
- Basic understanding of HTTP concepts (GET, POST, PUT, DELETE)
- Familiarity with JSON is helpful but not required

## 📦 Files Provided

- `starter-code.py` — minimal FastAPI scaffold with route examples
- `requirements.txt` — dependencies (FastAPI, Uvicorn)
- `README.md` — (this file) assignment instructions

## ⏱️ Estimated Time

75–120 minutes

## 🧭 Difficulty

Intermediate → Advanced

## 📝 Tasks

### 🛠️ Task 1 — Build the API Foundation

#### Description
Create a basic REST API with multiple endpoints that support CRUD operations (Create, Read, Update, Delete) for a simple resource (e.g., a book library, task manager, or blog posts).

#### Requirements
Completed API should:

- Define a data model or schema (use Pydantic for validation)
- Implement at least 4 endpoints: GET (list), GET (by ID), POST (create), DELETE or PUT (update/delete)
- Use appropriate HTTP status codes (200, 201, 400, 404, etc.)
- Store data in memory (a Python list or dictionary is fine for this assignment)
- Accept and return JSON data

Deliverable: a `main.py` or updated `starter-code.py` that runs via `uvicorn main:app --reload`

### 🛠️ Task 2 — Add Validation & Error Handling

#### Description
Enhance your API with input validation, meaningful error messages, and proper exception handling.

#### Requirements

- Use Pydantic models to validate request bodies
- Return clear error messages (e.g., validation errors, resource not found)
- Handle edge cases (duplicate entries, invalid IDs, empty fields)
- Test at least three error scenarios using a tool like `curl`, Postman, or the `/docs` Swagger UI

Deliverable: updated script and a short test report (`test-scenarios.txt` or `API-TESTING.md`) documenting errors tested.

### 🛠️ Task 3 — Documentation & Testing

#### Description
Document your API and write simple tests to verify core functionality.

#### Requirements

- Include endpoint descriptions and examples (use FastAPI's built-in Swagger docs at `/docs`)
- Write at least 3 unit tests or integration tests using `pytest`
- Add a short usage guide in a `USAGE.md` or in the README explaining how to run the server and make sample requests

Deliverable: `tests/test_api.py` (or similar) and a usage guide showing example curl or Python requests.

## 💡 Hints

- Use Pydantic `BaseModel` to define request/response schemas
- Leverage FastAPI's automatic Swagger UI at `/docs` for manual testing
- Use `@app.get()`, `@app.post()`, etc. decorators for route definitions
- For in-memory storage, a global list or dict works fine; you can migrate to a database later
- `uvicorn` auto-reloads when you save changes with the `--reload` flag

## ✅ Submission

1. Add your implementation to `starter-code.py` (or create `main.py`)
2. Include a `requirements.txt` with dependencies
3. Add `tests/test_api.py` with at least 3 test cases
4. Include `test-scenarios.txt` or `USAGE.md` with examples and error handling notes
5. Submit by creating a pull request or uploading the folder as instructed by the course

## 🎓 Learning Outcomes

- Understand REST API principles and HTTP methods
- Build a functional API using FastAPI and Pydantic
- Implement input validation and error handling
- Write tests to verify API behavior
- Use API documentation tools (Swagger/OpenAPI)
