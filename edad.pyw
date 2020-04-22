#Autor: Johan David Gomez Gil
#Correo: johang0297@gmail.com

import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import *

def calcular_edad(masaInicial,masaFinal,vidaMedia):

    prim = math.log(masaFinal/masaInicial)
    seg = math.log(2)
    x = (-vidaMedia*(prim)) / seg
    x = round(x,4)
    #print (x)
    return x

def graficar(masaInicial,masaFinal,vidaMedia):
    masaInicial = float(masaInicial)
    masaFinal = float(masaFinal)
    edad = calcular_edad(masaInicial,masaFinal,vidaMedia)
    texto = 'Interseccion (x = ',edad,' , y = 0)'
    x=np.linspace(-600,60000,10000) #Los dos primeros son el rango de X y el ultimo cuantos puntos se quieren
    #x=np.arange(14000,15000,1)

    plt.plot(x,h(x,masaInicial,masaFinal,vidaMedia))
    plt.grid(True)
    plt.text(edad,0,texto)
    v = [0,65000,-200,200]
    plt.axis(v)
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.show()

def h(x,masaInicial,masaFinal,vidaMedia):
    #expo = np.e ** ((-x*math.log(2))/5730)
    y = masaFinal - masaInicial *(np.e ** ((-x*math.log(2))/vidaMedia))
    return y




#----------------------------Interfaz grafica--------------------------------------------

def edad():

    raiz = Tk()

    raiz.title("Simulación")

    opciones = Frame()
    opciones.pack(side ="left")
    opciones.config(width = "100", height = "420", bd = 3,relief ="groove")

    tituloOpciones =  Label(opciones, text= "Opciones", font = (13))
    tituloOpciones.place(x=11,y=0)


    principal = Frame()
    principal.pack(side ="right")
    principal.config(width = "650", height = "450")

    masaInicial = Entry(principal)
    masaInicial.grid(row= 0, column = 1, pady = 10)
    tituloMasaInicial =  Label(principal, text= "Masa inicial: ", font = (13))
    tituloMasaInicial.grid(row= 0, column = 0,  padx = 20)



    masaActual = Entry(principal)
    masaActual.grid(row= 1, column = 1, pady = 10)
    tituloMasaActual =  Label(principal, text= "Masa actual: ", font = (13))
    tituloMasaActual.grid(row= 1, column = 0,  padx = 20)


    #----------------------RESULTADO-----------------------------------------------

    resultadoEdad = StringVar()

    resultado = Entry(principal, textvariable = resultadoEdad)
    resultado.grid(row= 2, column = 1, pady = 10, padx = 20)
    tituloResultado =  Label(principal, text= "Resultado: ", font = (13))
    tituloResultado.grid(row= 2, column = 0,  padx = 20)

    #-------Funcion para el boton calcular------------------------------------------

    def calcular(masaInicial,masaFinal,vidaMedia):

        masaIn = float(masaInicial)
        masaFin = float(masaFinal)
        resultado = calcular_edad(masaIn,masaFin,vidaMedia)
        resultadoEdad.set(resultado)

    botonCalcular = Button(principal, text = "Calcular", command= lambda: calcular(masaInicial.get(),masaActual.get(),5730))
    botonCalcular.grid(row= 2, column = 2, pady = 10)

    botonGraficar = Button(principal, text = "Graficar", command= lambda: graficar(masaInicial.get(),masaActual.get(),5730))
    botonGraficar.grid(row= 3, column = 0, pady = 10)
    botonGraficar.config(width = "10", height = "5")

    botonSalir = Button(principal, text = "Salir" , command = raiz.destroy)
    botonSalir.grid(row= 3, column = 1, pady = 10, columnspan=2)
    botonSalir.config(width = "10", height = "5")
    

    botonEdad = Button(opciones, text = "Calcular edad")
    botonEdad.place(x = 5, y= 30)
    

    botonVida = Button(opciones, text = "Calcular vida\n media")
    botonVida.place(x = 5, y= 60) 

    raiz.resizable(0,0)

    raiz.mainloop()

edad()