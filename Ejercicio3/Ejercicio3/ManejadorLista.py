import csv

from Registro import Registro


class ManejadorLista:

    def __init__(self):
        self.__ListaBidimensional=[]
        objetoRegistro = Registro()
        for i in range(30):
            lista = []
            for j in range(24):
                lista.append(objetoRegistro)
            self.__ListaBidimensional.append(lista)

    def retornalista(self):
        return (self.__ListaBidimensional)

    # def PruebaCarga(self): # test
    #     print("elemento 0 0 por defecto : ")
    #     print(self.__ListaBidimensional[0][0])
    #     print( "elemento 0 cambiado a 1")
    #     self.__ListaBidimensional[0][0] = 1
    #     print(self.__ListaBidimensional[0][0])
    #     print("elemento 0 1 por defecto")
    #     print(self.__ListaBidimensional[0][1])
    #     print("carga de un registro en la posicion 0 3")
    #     print("posicion 0 3 : ")
    #     print(self.__ListaBidimensional[0][3])
    #     print("carga reg")
    #     unregtemp = Registro(5.5, 4, 3.2)
    #     self.__ListaBidimensional[0][3] = unregtemp
    #     print(self.__ListaBidimensional[0][3])

    def AgregarAlaMatriz(self,dia,hora,registro):
        # if ((type(dia)==int)and(type(hora)==int)and(type(Registro)==Registro.Registro())):
        self.__ListaBidimensional[dia-1][hora] = registro


    # def CambiarTodoaEntero(self):
    #     for i in range(len(self.__ListaBidimensional)):
    #         for j, Registro in enumerate(self.__ListaBidimensional[i]):
    #             self.__ListaBidimensional[i][j] = 1


    def MostrarPorDia(self,dia):
        print("Hora Temperatura Humedad Presion")
        for hora in range(24):
             print("{} {} \n".format(hora,self.__ListaBidimensional[dia-1][hora]))

    # Es complicado especificar el día y hora de la mayor temperatura :
    # ...
    # def MayorTemperatura(self, diahora):
    #     max = self.__ListaBidimensional[0][0].getTemperatura()
    #     for i, ManejadorLista in enumerate(self.__ListaBidimensional):
    #         for j, ManejadorLista in enumerate(self.__ListaBidimensional[i]):
    #             if max < self.__ListaBidimensional[i][j].getTemperatura():
    #                 max = self.__ListaBidimensional[i][j].getTemperatura()
    #                 diahora[0]=i
    #                 diahora[1]=j
    #         print("del dia {} y hora {} temp max : {}".format(diahora[0], diahora[1], max))
    #     return (max)

    def MayorTemperatura(self):
        max = self.__ListaBidimensional[0][0].getTemperatura()
        for i, ManejadorLista in enumerate(self.__ListaBidimensional):
            for j, ManejadorLista in enumerate(self.__ListaBidimensional[i]):
                if max < self.__ListaBidimensional[i][j].getTemperatura():
                    max = self.__ListaBidimensional[i][j].getTemperatura()
        return (max)

    def MayorHumedad(self):
        max = self.__ListaBidimensional[0][0].getHumedad()
        for i, ManejadorLista in enumerate(self.__ListaBidimensional):
            for j, ManejadorLista in enumerate(self.__ListaBidimensional[i]):
                if max < self.__ListaBidimensional[i][j].getHumedad():
                    max = self.__ListaBidimensional[i][j].getHumedad()
        return (max)

    def MayorPresion(self):
        max = self.__ListaBidimensional[0][0].getpresion()
        for i,ManejadorLista in enumerate(self.__ListaBidimensional):
            for j,ManejadorLista in enumerate(self.__ListaBidimensional[i]):
                if max < self.__ListaBidimensional[i][j].getpresion():
                    max = self.__ListaBidimensional[i][j].getpresion()
        return (max)

    def MenorTemperatura(self):
        min = self.__ListaBidimensional[0][0].getTemperatura()
        for i, ManejadorLista in enumerate(self.__ListaBidimensional):
            for j,ManejadorLista in enumerate(self.__ListaBidimensional[i]):
                if min > self.__ListaBidimensional[i][j].getTemperatura():
                    min = self.__ListaBidimensional[i][j].getTemperatura()
        return (min)
    def MenorHumedad(self):
        min = self.__ListaBidimensional[0][0].getHumedad()
        for i,ManejadorLista in enumerate(self.__ListaBidimensional):
            for j, ManejadorLista in enumerate(self.__ListaBidimensional[i]):
                if min > self.__ListaBidimensional[i][j].getHumedad():
                    min = self.__ListaBidimensional[i][j].getHumedad()
        return (min)

    def MenorPresion(self):
        min = self.__ListaBidimensional[0][0].getpresion()
        for i,ManejadorLista in enumerate(self.__ListaBidimensional):
            for j, ManejadorLista in enumerate(self.__ListaBidimensional[i]):
                if min > self.__ListaBidimensional[i][j].getpresion():
                    min = self.__ListaBidimensional[i][j].getpresion()
        return (min)

    # def PromedioTempMensual(self): Promedio de todas las temperaturas, pero no por hora ...
    #     Prom=0.0
    #     contador=0
    #     for i, ManejadorLista in enumerate(self.__ListaBidimensional):
    #         for j,ManejadorLista in enumerate(self.__ListaBidimensional):
    #             Prom = Prom + self.__ListaBidimensional[i][j].getTemperatura()
    #             contador=contador+1
    #     Prom = float(Prom / contador)
    #     return Prom

    def PromedioPorHora(self,hora):
        prom=0.0
        contador=0
        for i in range(len(self.__ListaBidimensional)):
            prom = prom + self.__ListaBidimensional[i][hora].getTemperatura()
            contador = contador + 1
        return (prom/contador)

    def PromedioMensualPorHora(self):
        for hora in range(len(self.__ListaBidimensional)):
            print("Promedio Mensual de Temperaturas de la hora {} : {}".format(hora, self.PromedioPorHora(hora)))


    def ingresoArchivo(self):
        archivo = open('Temperaturas.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            dia = int(fila[0])
            hora = int(fila[1])
            temp = float(fila[2].replace(",", "."))
            hum = int(fila[3])
            pres = float(fila[4].replace(",", "."))
            regtemp = Registro(temp, hum, pres)
            self.__ListaBidimensional[dia-1][hora] = regtemp
        archivo.close()
