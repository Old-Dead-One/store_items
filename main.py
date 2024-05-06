from fastapi import FastAPI

from models import Store_Items

import json

app = FastAPI()

with open("store_items.json", "r") as f:
    data: list[dict] = json.load(f)

items: list[Store_Items] = []

for item in data:
    items.append(Store_Items(id=item["id"], name=item["name"], description=item["description"], price=item["price"]))

@app.get("/items")
async def get_items() -> list[Store_Items]:
    return items

@app.post("/items")
async def create_items(item: Store_Items) -> str:
    items.append(item)
    return ("{item} has been added successfully!")

@app.put("/items/{item_id}")
async def update_items(item_id: int, updated_item: Store_Items):
    for i, item in enumerate(items):
        if item.id == item_id:
            items[i] = updated_item
            return (f"Item with id {item_id} has been updated successfully!")
    
@app.delete("/items/{item_id}")
async def delete_items(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return (f"Item with id {item_id} has been deleted successfully!")
