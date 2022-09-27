import os
from tkinter import *
from tkinter import filedialog
import cv2
import cv2_ext
import time
import imghdr

pastaApp = os.path.dirname(__file__)

def AbrirImgClick():
    path = filedialog.askopenfile()
    if(path):
        im = cv2_ext.imread(path.name)
        r = cv2.selectROI(im)
        imgCortada = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        cv2.imshow("Imagem", imgCortada)
        extension = imghdr.what(path.name)
        SalvarImg(imgCortada, extension)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def SalvarImg(img, extension):
    directory = pastaApp + '\\assets'
    os.chdir(directory)
    fileName = 'imagem_' + str(time.time()) + '.' + extension
    print(directory)
    print(fileName)
    cv2.imwrite(fileName, img)