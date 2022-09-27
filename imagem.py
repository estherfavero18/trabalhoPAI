from tkinter import *
from tkinter import filedialog

from matplotlib.pyplot import text
from PIL import Image, ImageTk
import numpy as np
import cv2

import style
import imageHelper

# matriz para operar sobre a imagem
# tamanho das dimensões do canvas
# inicializada com 1 (cor branca)
matriz = np.ones((style.canvasWidth, style.canvasHeight))

# função chamada pelo botão btnOpenImg
# apresenta o filePicker e mostra a imagem dentro do Canvas
def openImgEvent():
    path = filedialog.askopenfilename()
    global image
    global image_for_mask_multiplication
    if path:
        image = Image.open(path)
        image_for_mask_multiplication = Image.open(path)
        image = image.resize((style.canvasHeight, style.canvasWidth), Image.Resampling.LANCZOS)
        image_for_mask_multiplication = image_for_mask_multiplication.resize((style.canvasHeight, style.canvasWidth), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)
        image_canvas.create_image(0, 0, image=image, anchor='nw')

# função bind do clique do mouse
# seta as coordenadas do clique, os primeiros pontos da linha
def getCoordenadas(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

# função bind da movimentação do mouse
# desenha a linha
def drawArea(event):
    global lasx, lasy # pega a última coordenada setada
    image_canvas.create_line((lasx, lasy, event.x, event.y), fill='red', width=3) # cria linha no canvas (último x, último, y, novo x, novo y)
    lasx, lasy = event.x, event.y # atualiza os últimos pontos x,y

    if lasx < style.canvasHeight and lasx >=0 and lasy < style.canvasWidth and lasy >=0: # valida se x,y estão dentro do limite
        # salva as coordenadas da linha para ter o molde da area recortada
        # seta os pixels de coordenada lasx, lasy e seus vizinhos com 0 (cor preta)
        matriz[lasy][lasx] = 0 
        matriz[lasy+1][lasx+1] = 0 
        matriz[lasy-1][lasx-1] = 0 
        matriz[lasy+1][lasx-1] = 0 
        matriz[lasy-1][lasx+1] = 0

# função chamada pelo botão btnSelectArea
# faz o bind dos eventos de clique e movimentação do mouse com suas respectivas funções
def selectAreaEvent():
    image_canvas.bind("<Button-1>", getCoordenadas)
    image_canvas.bind("<B1-Motion>", drawArea)

def returnArea(matrizImg):
    image = matrizImg
    gray = matrizImg

    matrizBorda = cv2.Canny(gray, 30, 200)
    contours, hierarchy = cv2.findContours(matrizBorda, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # procura o contono
    cv2.drawContours(image, contours, -1, (0, 0, 0), 3) # desenha o contorno
    T, thresImg = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY_INV) # ??
    floodFillImg = thresImg.copy()
    heigth, width = thresImg.shape[:2]
    matrizTemp = np.zeros((heigth + 2, width +2), np.uint8)
    cv2.floodFill(floodFillImg, matrizTemp, (0,0), (255,255,255))
    # cv2.imshow("Área preenchida de preto", floodFillImg)
    floodFillImg = np.abs(floodFillImg-np.ones((style.canvasWidth, style.canvasHeight))*255) # revertendo de preto para branco
    # cv2.imshow("Área preenchida de branco", floodFillImg)
    return floodFillImg

def cutAreaEvent():
    global image_for_mask_multiplication
    global img
    matriz3Canais = np.ones((style.canvasWidth, style.canvasHeight, 3)) 
    matrizUint = (matriz * 255).astype(np.uint8) # converte os elementos para uint
    mascara = returnArea(matrizUint)
    matriz3Canais[:,:,0] = mascara/255
    matriz3Canais[:,:,1] = mascara/255
    matriz3Canais[:,:,2] = mascara/255
    real_area = np.array(image_for_mask_multiplication) * matriz3Canais
    real_area = Image.fromarray(np.uint8(real_area)).convert('RGB')
    
    img = real_area.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)

    img.show()

def save_image():
    path_save = filedialog.asksaveasfilename()
    print(path_save)
    global img
    if path_save:
        img.save(str(path_save), "PNG")

stringT = "%s" % style.appWidth + "x%s" %style.appHeight
app = Tk()
app.title("Batata")
app.geometry(stringT)

title = Label(app, text="Corte de imagem", font="arial 30 bold", fg="#068481")
title.pack()

image_canvas = Canvas(app, width=style.canvasWidth, height=style.canvasHeight, bg=style.clBgBase)
image_canvas.pack(pady=(10,0))

btnOpenImg = Button(app, width=20, text="Abre a imagem", command=openImgEvent)
btnOpenImg.pack(pady=(10,5))

btnSelectArea = Button(app, width=20, text="Selecione a área", command=selectAreaEvent)
btnSelectArea.pack(pady=(0,5))

btnCutArea = Button(app, width=20, text="Corte a área", command=cutAreaEvent)
btnCutArea.pack(pady=(0,5))

btnSaveImg = Button(app, width=20, text="Salvar a imagem", command=save_image)
btnSaveImg.pack(pady=(0,5))

app.mainloop()