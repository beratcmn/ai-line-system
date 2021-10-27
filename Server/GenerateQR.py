import qrcode


class QRGenerator:

    ids = []

    def GenerateQR(self, _name: str, _surname: str, _id: int):
        datadict = {
            "name": _name,
            "surname": _surname,
            "id": str(_id)
        }

        datadict = str(datadict).replace("'", '"')
        print(datadict)

        img = qrcode.make(datadict)

        img.save(str(_id) + ".png")
