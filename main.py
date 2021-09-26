from dataclasses import dataclass
from QR_Reader import ScanQR
import time
import json

waitingUsers = []


@dataclass
class User:
    name: str
    id: str

    placeInLine = 0
    remainingTime = 0

    def renewTime(self):
        self.remainingTime = 1200  # saniye cinsinden kalan süre

    def decreaseTime(self):
        self.remainingTime = self.remainingTime - 1

        # TODO her 3 dakika da bir bütün kullanıcıları kontrol edip sürelerini azalt


def main():
    global waitingUsers

    scannedData = json.loads(ScanQR())

    user = User(name=scannedData["name"] + " " +
                scannedData["surname"], id=str(scannedData["id"]))

    print("len: " + str(len(waitingUsers)))
    if len(waitingUsers) == 0:
        waitingUsers.append(user)
        waitingUsers[waitingUsers.index(user)].renewTime()
        waitingUsers[waitingUsers.index(
            user)].placeInLine = len(waitingUsers)

        print("\nKullanıcı eklendi. \n")
    else:
        if user in waitingUsers:
            waitingUsers[waitingUsers.index(user)].renewTime()
            print("\nKullanıcı zaten tanımlı. \n")
        else:
            waitingUsers.append(user)
            waitingUsers[waitingUsers.index(user)].renewTime()
            waitingUsers[waitingUsers.index(
                user)].placeInLine = len(waitingUsers)
            print("\nKullanıcı eklendi. \n")

    print("-----------------------------")
    print("Şu an " + str(len(waitingUsers)) + " kişi sırada bekliyor.")
    print("-----------------------------")

    for i in waitingUsers:
        print("-----------------------------")
        print("İsim: " + str(i.name))
        print("Sıradaki Konumu: " + str(i.placeInLine))
        print("Kalan Süre: " + str(int(i.remainingTime / 60)) +
              " dakika " + str(int(i.remainingTime % 60)) + " saniye")
        print("-----------------------------")


while True:
    main()
