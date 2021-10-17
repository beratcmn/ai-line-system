import qrcode

datadict = {
    "name:": "Berat",
    "surname": "Çimen",
    "id": "0101"
}

img = qrcode.make(str(datadict))

img.save('user.png')
