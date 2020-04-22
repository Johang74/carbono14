#Autor: Johan David Gomez Gil
#Correo: johang0297@gmail.com

import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import *

def calcular_vida(masaInicial,masaFinal,tiempo):

    
    prim = math.log(2)
    seg = math.log(masaFinal/masaInicial)
    x = (-tiempo*(prim)) / seg
    x = round(x,4)
    #print (x)
    return x

def graficar(masaInicial,masaFinal,tiempo):
    masaInicial = float(masaInicial)
    masaFinal = float(masaFinal)
    tiempo = float(tiempo)
    vida = calcular_vida(masaInicial,masaFinal,tiempo)
    texto = 'Interseccion (x = ',vida,' , y = 0)'
    x=np.linspace(-60000,90000,10000) #Los dos primeros son el rango de X y el ultimo cuantos puntos se quieren
    #x=np.arange(14000,15000,1)

    plt.plot(x,h(x,masaInicial,masaFinal,tiempo))
    plt.grid(True)
    plt.text(vida,0,texto)
    v = [-500,65000,-200,200]
    plt.axis(v)
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.show()

def h(x,masaInicial,masaFinal,tiempo):
    #expo = np.e ** ((-x*math.log(2))/5730)
    y = masaFinal - masaInicial *(np.e ** ((-tiempo*math.log(2))/x))
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

    tiempo = Entry(principal)
    tiempo.grid(row= 2, column = 1, pady = 10)
    tituloTiempo =  Label(principal, text= "Tiempo: ", font = (13))
    tituloTiempo.grid(row= 2, column = 0,  padx = 20)


    #----------------------RESULTADO-----------------------------------------------

    resultadoEdad = StringVar()

    resultado = Entry(principal, textvariable = resultadoEdad)
    resultado.grid(row= 3, column = 1, pady = 10, padx = 20)
    tituloResultado =  Label(principal, text= "Resultado: ", font = (13))
    tituloResultado.grid(row= 3, column = 0,  padx = 20)

    #-------Funcion para el boton calcular------------------------------------------

    def calcular(masaInicial,masaFinal,tiempo):

        masaIn = float(masaInicial)
        masaFin = float(masaFinal)
        tiempo = float(tiempo)
        resultado = calcular_vida(masaIn,masaFin,tiempo)
        resultadoEdad.set(resultado)

    botonCalcular = Button(principal, text = "Calcular", command= lambda: calcular(masaInicial.get(),masaActual.get(),tiempo.get()))
    botonCalcular.grid(row= 3, column = 2, pady = 10)

    botonGraficar = Button(principal, text = "Graficar", command= lambda: graficar(masaInicial.get(),masaActual.get(),tiempo.get()))
    botonGraficar.grid(row= 4, column = 0, pady = 10)
    botonGraficar.config(width = "10", height = "5")

    botonSalir = Button(principal, text = "Salir" , command = raiz.destroy)
    botonSalir.grid(row= 4, column = 1, pady = 10, columnspan=2)
    botonSalir.config(width = "10", height = "5")
    

    botonEdad = Button(opciones, text = "Calcular edad")
    botonEdad.place(x = 5, y= 30)
    

    botonVida = Button(opciones, text = "Calcular vida\n media")
    botonVida.place(x = 5, y= 60)


    raiz.resizable(0,0)

    raiz.mainloop()

edad()