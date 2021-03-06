


from csv import reader
import csv
from infracciones import infracciones

from infractor import infractor

class ManejadorInfractores:

    def __init__(self):
        self.__listaInfractores = []

    

    def IngresoArchivo(self):
        archivo = open(r'/home/alumno/Descargas/hgs2022P1U2/infractores.csv')
        reader = csv.reader(archivo,delimiter = ';')
        next(reader)
        for fila in reader:

            dni = int(fila[0])
            nombre = str(fila[1])
            apellido = str(fila[2])
            direccion = str(fila[3])
            numero_carnet = int(fila[4])
            puntaje = int(fila[5])

            ObjetoInfractor = infractor(dni,nombre,apellido,direccion,numero_carnet,puntaje)
            self.__listaInfractores.append(ObjetoInfractor)
        archivo.close()

    def MostrarLista(self):
        print("Longitud lista : ",len(self.__listaInfractores))
        for i in self.__listaInfractores:
            print(i)

    def BuscarInfractorDNI(self,dni):
        i = 0
        dniencontrado = None
        while i<len(self.__listaInfractores) and self.__listaInfractores[i].getDni() != dni:
            i = i + 1
        if i<len(self.__listaInfractores):
            dniencontrado = self.__listaInfractores[i].getDni()
        return dniencontrado

    def DescuentoPuntos(self,ManejadorInfracciones):

        for i in range(len(self.__listaInfractores)):
            self.__listaInfractores[i].getDni()
            for j in range(len(ManejadorInfracciones.RetornaArregloLista())):
                if ManejadorInfracciones.RetornaArregloLista()[j].getDni() == self.__listaInfractores[i].getDni():
                    self.__listaInfractores[i].setPuntos()



    def Formato2(self,dni,ManejadorInfracciones):
        cont=0
        i=0
        while i<len(self.__listaInfractores) and self.__listaInfractores[i].getDni() != dni:
            i=i+1
        if i<len(self.__listaInfractores):
            SubTotal = 0
            Descuento = 0
            Total = 0
            print("\n")
            print("Infractor:")
            print(self.__listaInfractores[i].mostrardatos())
            print("\n")
            print("Infracciones:")
            for j in range (len(ManejadorInfracciones.RetornaArregloLista())):
                if self.__listaInfractores[i].getDni() == ManejadorInfracciones.RetornaArregloLista()[j].getDni():
                    print(ManejadorInfracciones.RetornaArregloLista()[j].mostrardatos())
                    SubTotal = SubTotal + ManejadorInfracciones.RetornaArregloLista()[j].getImporte()


            for k in range(len(ManejadorInfracciones.RetornaArregloLista())):
                if ManejadorInfracciones.RetornaArregloLista()[j] == ManejadorInfracciones.RetornaArregloLista()[k]:
                    cont = cont + 1
                    print("contador = ",cont)
            Descuento = 0
            if cont<=1:
                Descuento = SubTotal * 0.5
            
            

            Total = SubTotal - Descuento
            print("                             SubTotal : {}".format(SubTotal))
            print("                             Total : {}".format(Total))
            
            print("\n")

        