"""
FastAPI REST API Starter Code

This module provides a minimal scaffold for a REST API using FastAPI.
Extend this with your own endpoints and business logic.

Usage:
    uvicorn starter-code:app --reload

Then visit http://localhost:8000/docs to see the interactive API documentation.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="REST API",
    description="A simple REST API for managing resources",
    version="1.0.0"
)

# ============================================================================
# Pydantic Models (Data Schemas)
# ============================================================================

class ItemBase(BaseModel):
    """Base model for an item (book, task, post, etc.)"""
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    """Model for creating a new item"""
    pass

class Item(ItemBase):
    """Model for an item with an ID"""
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Example Item",
                "description": "This is an example item"
            }
        }

# ============================================================================
# In-Memory Database
# ============================================================================

# In production, use a real database; for this assignment, we use an in-memory list.
items_db: List[Item] = []
next_id = 1

# ============================================================================
# Root Endpoint
# ============================================================================

@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint. Returns a welcome message."""
    return {
        "message": "Welcome to the REST API",
        "docs_url": "http://localhost:8000/docs"
    }

# ============================================================================
# TODO: Add Your Endpoints Below
# ============================================================================

# GET /items - Retrieve all items
# TODO: Implement this endpoint

# GET /items/{item_id} - Retrieve a specific item by ID
# TODO: Implement this endpoint

# POST /items - Create a new item
# TODO: Implement this endpoint

# PUT /items/{item_id} - Update an item
# TODO: Implement this endpoint

# DELETE /items/{item_id} - Delete an item
# TODO: Implement this endpoint
