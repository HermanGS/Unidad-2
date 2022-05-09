import csv

from Registro import Registro


class ManejadorLista:
    __ListaBidimensional=[]


    def __init__(self):
        self.__ListaBidimensional=[]
        objetoRegistro = Registro()
        for i in range(30):
            lista = []
            for j in range(24):
                lista.append(objetoRegistro)
            self.__ListaBidimensional.append(lista)

    def PruebaCarga(self): # test
        print("elemento 0 0 por defecto : ")
        print(self.__ListaBidimensional[0][0])
        print( "elemento 0 cambiado a 1")
        self.__ListaBidimensional[0][0] = 1
        print(self.__ListaBidimensional[0][0])
        print("elemento 0 1 por defecto")
        print(self.__ListaBidimensional[0][1])
        print("carga de un registro en la posicion 0 3")
        print("posicion 0 3 : ")
        print(self.__ListaBidimensional[0][3])
        print("carga reg")
        unregtemp = Registro(5.5, 4, 3.2)
        self.__ListaBidimensional[0][3] = unregtemp
        print(self.__ListaBidimensional[0][3])

    def AgregarAlaMatriz(self,dia,hora,registro):
        # if ((type(dia)==int)and(type(hora)==int)and(type(Registro)==Registro.Registro())):
        self.__ListaBidimensional[dia-1][hora] = registro


    def CambiarTodoaEntero(self):
        for i in range(len(self.__ListaBidimensional)):
            for j, Registro in enumerate(self.__ListaBidimensional[i]):
                self.__ListaBidimensional[i][j] = 1


    def MostrarPorDia(self,dia):
        print("Hora Temperatura Humedad Presion")
        for hora in range(24):
             print("{} {} \n".format(hora,self.__ListaBidimensional[dia-1][hora]))


    def MayorTemperatura(self):
        max = self.__ListaBidimensional[0][0].getTemperatura()
        for i in range(self.__ListaBidimensional):
            for j in range(self.__ListaBidimensional[i]):
                if max < self.__ListaBidimensional[i][j].getTemperatura():
                    max = self.__ListaBidimensional[i][j].getTemperatura()
        return (max)

    def MayorHumedad(self):
        max = self.__ListaBidimensional[0][0].getHumedad()
        for i in range(self.__ListaBidimensional):
            for j in range(self.__ListaBidimensional[i]):
                if max < self.__ListaBidimensional[i][j].getHumedad():
                    max = self.__ListaBidimensional[i][j].getHumedad()

    def MayorPresion(self):
        max = self.__ListaBidimensional[0][0].getpresion()
        for i in range(self.__ListaBidimensional):
            for j in range(self.__ListaBidimensional[i]):
                if max < self.__ListaBidimensional[i][j].getpresion():
                    max = self.__ListaBidimensional[i][j].getpresion()

    def MenorTemperatura(self):
        min = self.__ListaBidimensional[0][0].getTemperatura()
        for i in range(self.__ListaBidimensional):
            for j in range(self.__ListaBidimensional[i]):
                if min > self.__ListaBidimensional[i][j].getTemperatura():
                    min = self.__ListaBidimensional[i][j].getTemperatura()

    def MenorHumedad(self):
        min = self.__ListaBidimensional[0][0].getHumedad()
        for i in range(self.__ListaBidimensional):
            for j in range(self.__ListaBidimensional[i]):
                if min > self.__ListaBidimensional[i][j].getHumedad():
                    min = self.__ListaBidimensional[i][j].getHumedad()

    def MenorPresion(self):
        min = self.__ListaBidimensional[0][0].getpresion()
        for i in range(self.__ListaBidimensional):
            for j in range(self.__ListaBidimensional[i]):
                if min > self.__ListaBidimensional[i][j].getpresion():
                    min = self.__ListaBidimensional[i][j].getpresion()




    def ingresoArchivo(self):
        archivo = open('Temperaturas.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            regtemp = Registro()
