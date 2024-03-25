from fastapi import *
from pydantic import BaseModel


app = FastAPI()


# class MyPassword(BaseModel):
#     my_password: str


@app.get("/")
def root():
    return {"Hello": "World"}
