import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('barcode.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('database.txt') as f:
    myDataList = f.read().splitlines()
print(myDataList)

while True:
    success, img = cap.read()
    code = decode(img)
    for barcode in code:
        if barcode in myDataList:
            print('Authorized')
        else:
            print('UnAuthorized')

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)

        # print(barcode.type)
    cv2.imshow('Result',img)
    cv2.waitKey(1)
    