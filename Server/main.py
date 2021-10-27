from typing import Counter
from fastapi import FastAPI
from fastapi.responses import FileResponse

from GenerateQR import QRGenerator

from dataclasses import dataclass

import random


# from Class.User import User # TODO MAKE IT WORK

# to start the server: python -m uvicorn main:app --reload


# <-- Declerations -->
app = FastAPI()

ids = []
users = []


@dataclass(init=True)
class User:
    name: str
    surname: str

    id = 0

    placeInLine = 0
    remainingTime = 0

    def SetID(self):
        self.id = random.randint(1000, 9999)
        while self.id in ids:
            self.id = random.randint(1000, 9999)

    def RenewTime(self):
        self.remainingTime = 1200  # saniye cinsinden kalan süre

    def DecreaseTime(self):
        self.remainingTime = self.remainingTime - 1


# <-- API Functions -->
@app.get("/")
def index():
    return {
        "Status": 0
    }


@app.get("/get-users/{user_id}")
def get_users(user_id):
    global users
    current = users[int(user_id) - 1]
    return {
        "Name": current.name,
        "Surname": current.surname,
        "ID": current.id
    }


@app.get("/get-ids")
def get_ids():
    global ids
    ids = []
    ids_names = {}
    for _user in users:
        ids_names[_user.name] = _user.id

    return ids_names


@app.post("/create-user/")
def create_user(_user: User):
    global users
    _user.SetID()
    users.append(_user)
    return {
        "Name": _user.name,
        "Surname": _user.surname,
        "ID": _user.id
    }
