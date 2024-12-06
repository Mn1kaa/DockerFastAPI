from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Docker": "FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = "Queonda"):
    return {"item_id": item_id, "q": q}
