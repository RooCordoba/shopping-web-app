from fastapi import FastAPI
from src.db import *
from src.endpoints import router

app = FastAPI()

db.connect()
db.create_tables([User])

app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}





