import csv
from ViajeroFrecuente import viajerofrecuente

class manejadorviajero:

    def __init__(self):
        self.__ListaViajeros = []

    def __str__(self):
        s = ""
        for viajero in self.__ListaViajeros:
            s = s+ str(viajero) + "\n"
        return (s)

    def retornaLista(self):
        return (self.__ListaViajeros)

    def retornaViajeroDeLista(self,num):
        return (self.__ListaViajeros[num])

    def AgregarViajeroaL(self,viajero):
        if (type(viajero)==viajerofrecuente):
            self.__ListaViajeros.append(viajero)

    def BuscarViajero(self,numero):
        viajero = None
        for i, viajerofrecuente in enumerate(self.__ListaViajeros):
            if(viajerofrecuente.retornaNUM()==numero):
                viajero=i
                return (viajero)
            else:
                print("No se encontro ningun viajero con ese numero")

    def testViajeros(self):
        archivo = open('Datos2.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            numeroV = int(fila[0])
            dni = int(fila[1])
            nombre = str(fila[2])
            apellido = str(fila[3])
            millasA = float(fila[4])
            unViajero = viajerofrecuente(numeroV,dni,nombre,apellido,millasA)
            self.AgregarViajeroaL(unViajero)
        archivo.close()

    def test(self):
        viajero1=viajerofrecuente(10, 3333333, "Miguel", "Punto", 50)
        viajero2=viajerofrecuente(11, 4333333, "Valentin", "Correa", 100)
        viajero3=viajerofrecuente(12, 5333333, "Lisandro", "Cabrera", 150)
        self.AgregarViajeroaL(viajero1)
        self.AgregarViajeroaL(viajero2)
        self.AgregarViajeroaL(viajero3)
