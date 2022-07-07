import numpy as np
import csv
from Novedades import Novedades
from ManejadorPersonal import ManejadorPersonal

class ManejadorNovedades:
    __ListaNovedades : list


    def __init__(self):
        self.__ListaNovedades = []

    def MostrarListaNovedades(self):
        for i in self.__ListaNovedades:
            print(i)


    def Ingresar_Novedades_Archivo(self,ManejadorPersoanal):
        
        ManejadorPersoanal.RetornaListaPersonal()
        archivo = open(r'C:\Users\HermanGS\Desktop\POO\novedades.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            legajo = int(fila[0])
            if ManejadorPersoanal.BuscarLegajo(legajo):
                importe = float (fila[1])
                concepto = str(fila[2])
                codigo = str(fila[3])
                ObjetoNovedad = Novedades(legajo,importe,concepto,codigo)
                self.__ListaNovedades.append(ObjetoNovedad)
        archivo.close()


    def SumatoriaLiquidar(self,legajo,sueldo):
        sumaAdicionales = 0.0
        sumaDescuentos = 0.0

        for i in range(len(self.__ListaNovedades)):
            if self.__ListaNovedades[i].getLegajo() == legajo:
                # print(self.__ListaNovedades[i].getLegajo())
                if self.__ListaNovedades[i].getCodigo() == 'A':
                    # print("Deberia ser A")
                    # print("Codigo = ",self.__ListaNovedades[i].getCodigo())
                    sumaAdicionales = sumaAdicionales  + self.__ListaNovedades[i].getImporte()
                    # print("sumaAdicionales = ",sumaAdicionales)
                if self.__ListaNovedades[i].getCodigo() == 'D':
                    sumaDescuentos = sumaDescuentos + self.__ListaNovedades[i].getImporte()
                    # print("sumaDescuentos = ",sumaDescuentos)

        # print("----------------------------------")
        # print("Resumen : ")
        # print("sumaAdicionales = ",sumaAdicionales)
        # print("sumaDescuentos = ",sumaDescuentos)

        sumatoria = sueldo + sumaAdicionales - sumaDescuentos
        return sumatoria

    def Listado(self,MP):
        
        for i in range(len(MP.RetornaListaPersonal())):
            print("----------------------------------")
            print(MP.RetornaListaPersonal()[i].Mostrardatos())
            print("\n")    
            print("codigo concepto importe")
            for j in range(len(self.__ListaNovedades)):
                if MP.RetornaListaPersonal()[i].getLegajo() == self.__ListaNovedades[j].getLegajo():
                    print(self.__ListaNovedades[j].Mostrardatos())
            MP.RetornaListaPersonal()[i].getSueldo()
            Sumatoria = self.SumatoriaLiquidar(MP.RetornaListaPersonal()[i].getLegajo(),MP.RetornaListaPersonal()[i].getSueldo())
            print("TOTAL : {}".format(Sumatoria))
            print("----------------------------------")


