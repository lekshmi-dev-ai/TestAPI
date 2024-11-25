from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User1(BaseModel):
    id1: int
    name1: str
    email1: str

users = []

@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API"}

@app.get("/users", response_model=List[User1])
async def get_users():
    return users

@app.post("/users", response_model=User1)
async def add_user(user: User1):
    users.append(user)
    return user





'''app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

    '''