import numpy as np
from infracciones import infracciones
import csv

class ManejadorInfracciones:

    def __init__(self):
        self.__ArregloInfracciones = np.empty(0,dtype = infracciones )

    def IngresoArchivo(self,ManejadorInfractores):
        
        
        archivo = open(r'/home/alumno/Descargas/hgs2022P1U2/infracciones.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)

        for fila in reader:

            dni = int (fila[0])
            if ManejadorInfractores.BuscarInfractorDNI(dni) != None:
                patente = str(fila[1])
                tipovehiculo = str(fila[2])
                marca = str(fila[3])
                fecha = str(fila[4])
                descripcion = str(fila[5])
                importeAPagar = float(fila[6])
                estado = str(fila[7])

                ObjetoInfracciones = infracciones(dni,patente,tipovehiculo,marca,fecha,descripcion,importeAPagar,estado)
                self.__ArregloInfracciones = np.append(self.__ArregloInfracciones,ObjetoInfracciones)

    def MostrarArreglo(self):
        print("Longitud lista : ",len(self.__ArregloInfracciones))
        for i in self.__ArregloInfracciones:
            print(i)

    def RetornaArregloLista(self):
        return self.__ArregloInfracciones