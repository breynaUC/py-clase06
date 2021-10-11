from tkinter import *
from typing import Sized
ventana = Tk()
horas = IntVar()
hextras = IntVar()
salario = IntVar()
ht= 0
ph = 35 #pago hora regular
pe = 40 #pago por hora extra
hee = 0;
jornada = 48
pago = 0
def calcular():
    ht = horas.get()
    if ht > jornada:
        hee = ht - jornada
        pago = ph * jornada + hee*pe
        hextras.set(hee)
        salario.set(pago)
    else:
        print(ht*ph)
        salario.set(ph*ht)

ventana.geometry("800x400")
ventana.title("Desarrollo de Ejercicios")
enunciado = Label(ventana, text="Ejercicio 7")
enunciado.pack()
t1 = Label(ventana, text="Horas Trabajadas:")
t1.pack()
caja1 = Entry(ventana, textvariable=horas)
caja1.pack()
caja2 = Entry(ventana, textvariable=hextras)
caja2.pack()
caja2 = Entry(ventana, textvariable=salario)
caja2.pack()
boton1 = Button(ventana, text="Calcular Sueldo", command=calcular)
boton1.pack()
boton2 = Button(ventana, text="Salir", command=ventana.quit)
boton2.pack(side="left")
ventana.mainloop()