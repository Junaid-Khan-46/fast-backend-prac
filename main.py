from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

arr_items = []
@app.post("/items/")
def create_item(item: Item):
    arr_items.append(item)
    return item

@app.get("/items/")
def read_items():
    return arr_items

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    arr_items[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    arr_items.pop(item_id)
    return {"message": "Item deleted successfully"}

@app.patch("/items/{item_id}")
def partial_update_item(item_id: int, item: Item):
    arr_items[item_id] = item
    return item
