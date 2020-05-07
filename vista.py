from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np 
import matplotlib.pyplot as plt
import math


class vida:

    def __init__(self,ventana):
        self.wind = ventana
        self.wind.title("Simulacion")
        self.vidaMedia = 5730 #Vida media del carbono 14

        frame = LabelFrame(self.wind, text = 'Simulacion')
        frame.grid(row = 1, column = 2, padx = 5)       

        Label(frame, text = 'Masa inicial: ').grid(row = 1, column = 1)
        self.masaInicial = ttk.Entry(frame)
        self.masaInicial.focus()
        self.masaInicial.grid(row = 1, column = 2, pady = 5)

        Label(frame, text = 'Masa actual: ').grid(row = 2, column = 1)
        self.masaActual = ttk.Entry(frame)
        self.masaActual.grid(row = 2, column = 2, pady = 5)

        Label(frame, text = 'Resultado: ').grid(row = 3, column = 1)
        self.resultadoEdad = StringVar()
        self.resultado = ttk.Entry(frame, textvariable = self.resultadoEdad)
        self.resultado.grid(row = 3, column = 2, pady = 5)

        self.bGraficar = ttk.Button(frame, text = 'Graficar', width = 20, command = lambda: self.graficar())
        self.bGraficar.grid(row = 4, column = 1, pady = 5, rowspan = 2, sticky = 'EWNS', columnspan = 2)
        
        self.bSalir = ttk.Button(frame, text = 'Salir', width = 20, command = self.wind.destroy)
        self.bSalir.grid(row = 4, column = 3, pady = 5, rowspan = 2, sticky = 'EWNS', columnspan = 2)

        self.bCalcular = ttk.Button(frame, text = 'Calcular', command = lambda: self.Calcular())
        self.bCalcular.grid(row = 3, column = 4, pady = 5, padx = 3)

    #-----------------------------Funciones-----------------------------------------

    def f(self,x,masaInicial,masaFinal):
        y = masaFinal - masaInicial *(np.e ** ((-x*math.log(2))/self.vidaMedia))
        return y
    
    
    def calcularEdad(self, masaInicial, masaFinal):
        prim = math.log(masaFinal/masaInicial)
        seg = math.log(2)
        x = (-self.vidaMedia*(prim)) / seg
        x = round(x,4)
        return x

    def Calcular(self):
        masaIn = float(self.masaInicial.get())
        masaFin = float(self.masaActual.get())
        resultado = self.calcularEdad(masaIn, masaFin)
        self.resultadoEdad.set(resultado)

    def graficar(self):
        masaIn = float(self.masaInicial.get())
        masaFin = float(self.masaActual.get())
        edad = self.calcularEdad(masaIn, masaFin)
        self.resultadoEdad.set(edad)
        texto ='\nM0= '+str(masaIn) + '\nM(t)= '+str(masaFin) +'\nEdad: '+ str(edad)

        x = np.linspace(-600,60000,10000)          
        plt.plot(x,self.f(x, masaIn, masaFin), label = texto)    
        #plt.plot(x,self.f(x, masaIn+50, masaFin+50),'--', label ='Secundaria') 
        plt.title('Edad de la muestra')
        plt.legend(loc = 4)
        v = [0,65000,-200,200]
        plt.axis(v)
        plt.ylabel('Y')
        plt.xlabel('AÑOS')
        plt.grid(True)
        plt.show()