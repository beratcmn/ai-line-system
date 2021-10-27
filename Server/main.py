from typing import Counter
from fastapi import FastAPI
from fastapi.responses import FileResponse

from GenerateQR import QRGenerator

from dataclasses import dataclass

# from Class.User import User # TODO MAKE IT WORK

# to start the server: python -m uvicorn main:app --reload


# <-- Declerations -->
app = FastAPI()


@dataclass
class User:
    name: str
    surname: str
    id: str

    placeInLine = 0
    remainingTime = 0

    def RenewTime(self):
        self.remainingTime = 1200  # saniye cinsinden kalan süre

    def DecreaseTime(self):
        self.remainingTime = self.remainingTime - 1


test_user = User("Berat", "Çimen", 210217017)
users = [test_user]  # user list   #old_id and object pairs


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
