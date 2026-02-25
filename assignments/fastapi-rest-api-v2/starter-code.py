from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI Starter - Items API")


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    price: float = Field(..., ge=0)


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int


# In-memory store
_items: List[Item] = []
_next_id = 1


@app.get("/items", response_model=List[Item])
def list_items():
    return _items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in _items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global _next_id
    item = Item(id=_next_id, **payload.dict())
    _next_id += 1
    _items.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate):
    for idx, it in enumerate(_items):
        if it.id == item_id:
            updated = Item(id=item_id, **payload.dict())
            _items[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for idx, it in enumerate(_items):
        if it.id == item_id:
            _items.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Item not found")
