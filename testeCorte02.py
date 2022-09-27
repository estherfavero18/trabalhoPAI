from pkgutil import ImpImporter
import cv2_ext
import cv2
from tkinter import filedialog
import numpy as np
import imghdr

if __name__ == '__main__' :
    path = filedialog.askopenfile()
    pathName = path.name
    print(path)
    print(pathName)
    if(path):
        teste = imghdr.what(pathName)
        print(teste)
        # Read image
        # im = cv2.imread("assets/soccer_practice.jpg")
        im = cv2_ext.imread(pathName)
        # Select ROI
        r = cv2.selectROI(im)

        # Crop image
        imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

        # Display cropped image
        cv2.imshow("Image", imCrop)
        cv2.waitKey(0)