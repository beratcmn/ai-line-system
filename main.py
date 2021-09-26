from dataclasses import dataclass
from QR_Reader import ScanQR
import time
import json


@dataclass
class User:
    name: str
    placeInLine: int
    id: int

    remainingTime = 0

    def renewTime(self):
        self.remainingTime = 1200  # saniye cinsinden kalan süre

    def decreaseTime(self):
        self.remainingTime = self.remainingTime - 1

        # TODO her 3 dakika da bir bütün kullanıcıları kontrol edip sürelerini azalt


waitingUsers = []


def main():
    global waitingUsers

    scannedData = json.loads(ScanQR())

    user = User(name=scannedData["name"] + " " + scannedData["surname"],
                placeInLine=len(waitingUsers) + 1, id=scannedData["id"])

    if len(waitingUsers) != 0:
        for i in waitingUsers:
            if i.id == user.id:
                i.renewTime()
                print("Kullanıcı zaten tanımlı.")
            else:
                waitingUsers.append(user)
                user.renewTime()
                print("Kullanıcı eklendi.")
    elif len(waitingUsers) == 0:
        waitingUsers.append(user)
        user.renewTime()
        print("Kullanıcı eklendi.")

    print("Şu an " + str(len(waitingUsers)) + " kişi sırada bekliyor.")

    for i in waitingUsers:
        print("-----------------------------")
        print("İsim: " + str(i.name))
        print("Sıradaki Konumu: " + str(i.placeInLine))
        print("Kalan Süre: " + str(int(i.remainingTime / 60)) +
              " dakika " + str(int(i.remainingTime % 60)) + " saniye")


while True:
    main()
