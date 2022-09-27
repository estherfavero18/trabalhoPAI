from email import message
from tkinter import *
from tkinter import messagebox

from matplotlib.pyplot import text
import style
import os

pastaApp = os.path.dirname(__file__)

def semComando():
    print("")

def abrirPaginaForm():
    exec(open(pastaApp+"\\form.py").read(), {'x':10})

def mostrarMsg(tipo, msg):
    if(tipo == "1"):
        messagebox.showinfo(title="Informação", message=msg)
    elif(tipo == "2"):
        messagebox.showwarning(title="Warning", message=msg) 
    elif(tipo == "3"):
        messagebox.showerror(title="Warning", message=msg)

def resetTxt():
    res=messagebox.askyesno("Confirmação", "Sim ou não?")
    if(res==True):
        vlTxt.delete(0,END)
        vlTxt.insert(0,"1")


app = Tk()
app.title("Batata")
app.geometry("500x300")
app.configure(background=style.clBgBase)

menuBar = Menu(app)
menuForm = Menu(menuBar, tearoff=0)
menuForm.add_command(label="Form", command=abrirPaginaForm)
menuForm.add_command(label="Item", command=semComando)
menuForm.add_separator()
menuForm.add_command(label="Fechar", command=app.quit)
menuBar.add_cascade(label="Menu", menu=menuForm)

app.config(menu=menuBar)

varTpMsg = StringVar()

Label(app,text="Tipo de msg(1,2,3)", background=style.clBgBase, foreground=style.clFgBase, anchor=W).pack()
vlTxt = Entry(app, textvariable=varTpMsg)
varTpMsg.set("1")
vlTxt.pack()

mensagem = "Olá, olha aê"
btnMsg = Button(app, text="Mostrar mensagem", command=lambda:mostrarMsg(varTpMsg.get(), mensagem))
btnMsg.pack()

btnMsg = Button(app, text="Resetar", command=resetTxt)
btnMsg.pack()

app.mainloop()