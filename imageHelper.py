from tkinter import *
from tkinter import filedialog

from matplotlib import image
from PIL import Image, ImageTk
import style

def showFilePicker():
    path = filedialog.askopenfilename()
    global image
    global image_for_mask_multiplication
    if path:
        image = Image.open(path)
        image_for_mask_multiplication = Image.open(path)
        image = image.resize((style.canvasWidth, style.canvasHeight), Image.Resampling.LANCZOS)
        image_for_mask_multiplication = image_for_mask_multiplication.resize((500, 490), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        return image, image_for_mask_multiplication
    return None
