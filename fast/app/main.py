from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    print("hello world")
    return {"Hello": "World"}


@app.get("/hello")
def read_fastapi_hello():
    print("hello FastAPI")
    return {"Hello": "FastAPI"}


@app.get("/items/{item_id}/{xyz}")
def read_item(item_id: int, xyz: str, q: Optional[str] = None):
    return {"item_id": item_id, "xyz": xyz, "q": q}
