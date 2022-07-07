from pickle import TRUE
import numpy as np
import csv
from Personal import Personal

class ManejadorPersonal:
    __ArregloPersonal = []


    def __init__(self):
        self.__ArregloPersonal = np.empty(0,dtype=Personal)
        
    def AgregarPersonal(self,personal):
        self.__ArregloPersonal = np.append(self.__ArregloPersonal,personal)

    def MostrarArregloPersonal(self):
        for i in self.__ArregloPersonal:
            print(i)

    def RetornaListaPersonal(self):
        return self.__ArregloPersonal

    def Ingresar_Personal_Archivo(self):
        archivo = open(r'C:\Users\HermanGS\Desktop\POO\personal.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            legajo = int(fila[0])
            dni = int(fila[1])
            apellido = str(fila[2])
            nombre = str(fila[3])
            sueldo_basico = float(fila[4])
            
            ObjetoPersonal = Personal(legajo,dni,apellido,nombre,sueldo_basico)
            self.AgregarPersonal(ObjetoPersonal)

        archivo.close()

    def BuscarLegajo(self,legajo):
        
        i = 0
        LegajoObtenido = False
        while i<len(self.__ArregloPersonal) and self.__ArregloPersonal[i].getLegajo() != legajo:
            i=i+1
        if i<len(self.__ArregloPersonal):
            LegajoObtenido = True
        return LegajoObtenido


    def RetornaLegajo(self,legajo):
        
        i = 0
        LegajoObtenido = None
        while i<len(self.__ArregloPersonal) and self.__ArregloPersonal[i].getLegajo() != legajo:
            i=i+1
        if i<len(self.__ArregloPersonal):
            LegajoObtenido = self.__ArregloPersonal[i].getLegajo()
        return LegajoObtenido
    
    def ObtenerSueldoPorLegajo(self,legajo):
        
        i = 0
        sueldoBasico = None
        while i<len(self.__ArregloPersonal) and self.__ArregloPersonal[i].getLegajo() != legajo:
            i=i+1
        if i<len(self.__ArregloPersonal):
            sueldoBasico = self.__ArregloPersonal[i].getSueldo()
        return sueldoBasico


    def Ordenamiento2(self):
        self.__ArregloPersonal.sort()
    

    def Ordenamiento3(self):
        np.sort(self.__ArregloPersonal,order='nombre')

    def Ordenamiento(self):
        for i in range(len(self.__ArregloPersonal)):
            try:
                if i != len(self.__ArregloPersonal):
                    if self.__ArregloPersonal[i] > self.__ArregloPersonal[i+1]: 
                        aux = self.__ArregloPersonal[i+1]
                        self.__ArregloPersonal[i+1] = self.__ArregloPersonal[i]
                        self.__ArregloPersonal[i] = aux
            except StopIteration:
                    print("s")

    def Minimo(self):
        minimo = self.__ArregloPersonal[0]
        for i in range(len(self.__ArregloPersonal)):
                if self.__ArregloPersonal[i] < minimo:
                    minimo = self.__ArregloPersonal[i]
        return minimo
