from fastapi import FastAPI, Body, Request, Header, Depends, APIRouter
from passlib.hash import pbkdf2_sha256

from pydantic import BaseModel
class Person(BaseModel):
    name: str
    age: int

persons = [
    Person(name="jake", age=3),
    Person(name="jane", age=4)
]
app = FastAPI()
account_router = APIRouter(prefix="/account")

def user_dep(username: str = Body(embed=True), password: str = Body(embed=True)):
    return {"user": username, "password": pbkdf2_sha256.hash(password)}

@account_router.post("/login/")
def hello(
        user: dict = Depends(user_dep),
):
    return user
app.include_router(account_router)
