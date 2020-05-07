from tkinter import Tk, mainloop
from vista import *



def interfaz():
    ventana = Tk()
    res = vida(ventana)
    ventana.mainloop()
    


if __name__ == "__main__":
    interfaz()