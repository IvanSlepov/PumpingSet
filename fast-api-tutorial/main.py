from fastapi import *
import requests
import json
import xmltojson
import httpx
from pydantic import BaseModel

app = FastAPI()


# @app.get("/")
# def access_test_page():
#     api_url = "http://mytestvmone.com/"
#     return api_url

messages: list = []


@app.get("/")
def root() -> dict[str, str]:
    return {"Here we go": "again"}


@app.post("/messages")
def post_message(new_message: str) -> list:
    messages.append(new_message)
    return messages


@app.get("/messages/{message_id}")
def get_message(message_id: int) -> str:
    message = messages[message_id]
    return message


@app.put("/update-message/{message_id}")
def get_message(message_id: int, updated_message: str) -> list:
    messages[message_id] = updated_message
    return messages


@app.delete("/delete-message/{message_id}")
def get_message(message_id: int) -> list:
    messages.remove(messages[message_id])
    return messages
