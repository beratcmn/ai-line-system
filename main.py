from dataclasses import dataclass
from QR_Reader import ScanQR
import time
import json

waitingUsers = []


@dataclass
class User:
    name: str
    placeInLine: int

    remainingTime = 0

    def renewTime(self):
        self.remainingTime = 1200  # saniye cinsinden kalan süre

    def decreaseTime(self):
        self.remainingTime = self.remainingTime - 1


def main():
    scannedData = json.loads(ScanQR())

    user = User(name=scannedData["name"] + " " + scannedData["surname"],
                placeInLine=len(waitingUsers) + 1)

    if user not in waitingUsers:
        waitingUsers.append(user)
        user.renewTime()
    else:
        user.renewTime()

    print(waitingUsers)

while True:
    main()
