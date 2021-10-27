import qrcode
import random


class QRGenerator:

    ids = []

    def GenerateQR(self, _name: str, _surname: str):
        _id = random.randint(1000, 9999)
        while _id in self.ids:
            _id = random.randint(1000, 9999)

        datadict = {
            "name": _name,
            "surname": _surname,
            "id": str(_id)
        }

        datadict = str(datadict).replace("'", '"')
        print(datadict)
        img = qrcode.make(datadict)

        img.save('user.png')
