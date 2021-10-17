import qrcode
import random


def GenerateQR(_name: str, _surname: str):
    _id = random.randint(1000, 9999)
    datadict = {
        "name:": _name,
        "surname": _surname,
        "id": str(_id)
    }

    print(str(datadict))
    img = qrcode.make(str(datadict))

    img.save('user.png')
