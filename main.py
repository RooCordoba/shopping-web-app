from fastapi import FastAPI
from src.db import *
from src.endpoints import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}





