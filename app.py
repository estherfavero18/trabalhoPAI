from tkinter import *
from tkinter import filedialog

from matplotlib.pyplot import text
from PIL import Image, ImageTk
import numpy as np
import cv2

import style
import fileHelper

stringT = "%s" % style.appWidth + "x%s" %style.appHeight
app = Tk()
app.title("Batata")
app.geometry(stringT)

# Criação do menu
menuBar = Menu(app)
menu = Menu(menuBar, tearoff=0)
menu.add_command(label="Selecionar", command=fileHelper.AbrirImgClick),
menuBar.add_cascade(label="Menu", menu=menu)
app.config(menu=menuBar)

app.mainloop()