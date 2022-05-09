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

    def PruebaCarga(self): # La carga si funciona , el print de la lista muestra todos ceros a pesar de que si esta cargada
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
            for j in range(len(self.__ListaBidimensional)):
                self.__ListaBidimensional[i][j] = 1


    def mostrarTODOxd(self):
        print(len(self.__ListaBidimensional))


    def MostrarPorDia(self,dia):
       # print(hora) la hora no es el problema
            # este método imprime el mismo elemento de la lista en todo el for
            #  en vez de imprimir toda la lista
            # unregtemp = Registro(5.5, 4, 3.2)
            # self.__ListaBidimensional[dia][hora] = unregtemp
        print("dia : ")
        print(dia)
        print("Hora Temperatura Humedad Presion")
        for i in range(24):
            # print("{} {} \n".format(i, self.__ListaBidimensional[dia][i]))
            print("{} {} \n".format(i,self.__ListaBidimensional[dia-1][i]))


    def ingresoArchivo(self):
        archivo = open('Temperaturas.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            regtemp = Registro()
