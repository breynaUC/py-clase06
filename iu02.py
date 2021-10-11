from tkinter import *
ventana = Tk()
ventana.geometry("800x400")
numero = IntVar()
resultado = StringVar()
num = 0
def calcular():
    num = numero.get()
    if num%2==0:
        resultado.set("PAR")
    else:
        resultado.set("IMPAR")

n1 = Entry(ventana, textvariable=numero)
n1.pack()
r = Entry(ventana, textvariable=resultado)
r.pack()
b = Button(ventana, text="Calcular", command=calcular)
b.pack()
ventana.mainloop()