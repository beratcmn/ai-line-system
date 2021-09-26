import cv2
import numpy as np
from pyzbar.pyzbar import decode


def ScanQR():
    def decoder(image):
        gray_img = cv2.cvtColor(image, 0)
        barcode = decode(gray_img)

        for obj in barcode:
            points = obj.polygon
            (x, y, w, h) = obj.rect
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)

            barcodeData = obj.data.decode("utf-8")

            return barcodeData

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        returnData = decoder(frame)
        cv2.imshow('Yüz Tanıma Sistemi', frame)
        code = cv2.waitKey(10)
        if code == ord('q'):
            break
        if returnData != None:
            return returnData
