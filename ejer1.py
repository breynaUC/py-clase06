from tkinter import *
ventana = Tk()
ventana.title("Mi Primer Ejemplo")


boton1 = Button(ventana, text="Salir", command=ventana.quit)
boton1.pack(side="right")
ventana.mainloop()