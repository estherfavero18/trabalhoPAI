from tkinter import *

_clBgBase = "#778899"
_clFgBase = "#fff"
_clBlue = "#008"

print(x)

def impDados():
    print("Label: %s" % vlLabel.get())
    print("Text: %s" % vlText.get("1.0", END))


app = Tk()
app.title("Batata")
app.geometry("500x300")
app.configure(background=_clBgBase)


# txt1 = Label(app,text="Lorem ipsum", background=_clBgBase, foreground=_clFgBase)
# txt1.place(x=10, y=10, width=100, height=20)

# txt2 = Label(app,text="Lorem ipsum Dois", background=_clBlue, foreground=_clFgBase)
# txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=X, expand=True)

Label(app,text="Label Entry", background=_clBgBase, foreground=_clFgBase, anchor=W).place(x=10, y=10, width=100, height=20)
vlLabel = Entry(app)
vlLabel.place(x=10, y=30, width=200, height=20)

Label(app,text="Label Text", background=_clBgBase, foreground=_clFgBase, anchor=W).place(x=10, y=60, width=100, height=20)
vlText = Text(app)
vlText.place(x=10, y=80, width=200, height=80)

Button(app, text="Imprimir", command=impDados).place(x=10, y=270, width=100, height=20)

app.mainloop()