from tkinter import *
ventana = Tk()
ventana.geometry("800x400")
edad = IntVar()
resultado = StringVar()
num = 0
def calcular():
    num = edad.get()
    if num>18:
        resultado.set("MAYOR DE EDAD")
    else:
        resultado.set("MENOR DE EDAD")

n1 = Entry(ventana, textvariable=edad)
n1.pack()
r = Entry(ventana, textvariable=resultado)
r.pack()
b = Button(ventana, text="Calcular", command=calcular)
b.pack()
ventana.mainloop()