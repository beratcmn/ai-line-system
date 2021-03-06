from QR_Reader import ScanQR
from GenerateQR import GenerateQR
from User import User
import tkinter as tk
import tkinter.font as tkFont
import time
import json
from multiprocessing import Process
import multiprocessing
import sqlite3 as sl


waitingUsers = []


""" def ScanAndAddUser():
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
        print("-----------------------------") """


def ScanAndAddUser():
    global waitingUsers

    scannedData = json.loads(ScanQR())
    scannedData = dict(scannedData)

    newUser = User(name=str(scannedData["name"]),
                   surname=str(scannedData["surname"]),
                   id=str(scannedData["id"]))
    if len(waitingUsers) == 0:
        waitingUsers.append(newUser)
        newUser.RenewTime()
    else:
        if newUser in waitingUsers:
            newUser.RenewTime()

    for user in waitingUsers:
        print(user.name)
        print(user.surname)
        print(user.id)
        print(user.remainingTime)
        print(user.placeInLine)


def createUserButton_command():
    GenerateQR("Berat", "Çimen")


def scanUserButton_command():
    # Process(target=ScanAndAddUser).start().join()
    # Process(target=ScanAndAddUser).join()
    ScanAndAddUser()


def DecreaseAllTime():
    global waitingUsers
    while True:
        if len(waitingUsers) != 0:
            for _user in waitingUsers:
                _user.DecreaseTime()
                print(_user.remainingTime)
                time.sleep(1)
        else:
            #print("Kullanıcı bulunamadı.")
            time.sleep(1)


def GenerateGUI():
    root = tk.Tk()
    root.title("Sıra Kontrol Sistemi")
    root.iconbitmap("icon.ico")
    width = 600
    height = 500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height,
                                (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    GLabel_725 = tk.Label(root)
    GLabel_725["cursor"] = "arrow"
    ft = tkFont.Font(family='Times', size=22)
    GLabel_725["font"] = ft
    GLabel_725["fg"] = "#333333"
    GLabel_725["justify"] = "center"
    GLabel_725["text"] = "Versiyon 0.1"
    GLabel_725.place(x=220, y=0, width=150, height=44)

    createUserButton = tk.Button(root)
    createUserButton["activebackground"] = "#393d49"
    createUserButton["bg"] = "#01aaed"
    ft = tkFont.Font(family='Times', size=22)
    createUserButton["font"] = ft
    createUserButton["fg"] = "#ffffff"
    createUserButton["justify"] = "center"
    createUserButton["text"] = "Kullanıcı Oluştur"
    createUserButton["relief"] = "flat"
    createUserButton.place(x=80, y=120, width=200, height=200)
    createUserButton["command"] = createUserButton_command

    scanUserButton = tk.Button(root)
    scanUserButton["activebackground"] = "#393d49"
    scanUserButton["bg"] = "#00ced1"
    scanUserButton["cursor"] = "arrow"
    ft = tkFont.Font(family='Times', size=22)
    scanUserButton["font"] = ft
    scanUserButton["fg"] = "#ffffff"
    scanUserButton["justify"] = "center"
    scanUserButton["text"] = "Kullanıcı Tara"
    scanUserButton["relief"] = "flat"
    scanUserButton.place(x=330, y=120, width=200, height=200)
    scanUserButton["command"] = scanUserButton_command
    root.mainloop()


def CollectUsers():
    con = sl.connect("users.db")

    try:
        with con:
            con.execute("""
                CREATE TABLE USER (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    surname TEXT
                );
            """)
    except:
        pass

    data = con.execute("SELECT * FROM USER")
    print(data)

# GenerateGUI()

# threading.Thread(target=GenerateGUI).start()
# threading.Thread(target=DecreaseAllTime).start()
# GenerateGUI()


processes = []

process_time_decrease = Process(target=DecreaseAllTime)
process_generate_gui = Process(target=GenerateGUI)
process_collect_users = Process(target=CollectUsers)

processes.append(process_time_decrease)
processes.append(process_generate_gui)
processes.append(process_collect_users)


if __name__ == "__main__":
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    # TODO find a way to share data between threads
    # TODO Method 1: perotically write data to a local file (like txt) then read it from other process
