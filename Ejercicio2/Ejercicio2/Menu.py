from ViajeroFrecuente import viajerofrecuente

class Menu:
    __opciones = {}
    def opciones(self):
        self.__opciones = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.salida
        }
    def opcion(self,op,viajero):
        f = self.__opciones.get(op,lambda: print("Opción Incorrecta") )
        if (op=='1'or op=='2' or op== '3'):
            f(viajero)
        else:
            f()



    def opcion1(self,viajero):
        print("Cantidad Total de millas : {}".format(viajero.cantidadTotaldeMillas()))

    def opcion2(self,viajero):
        print("Cantidad de millas Actuales despues de la Suma : {}".format(viajero.acumularMillas(int(input("Ingrese la cantidad de millas que ha recorrido para acumular : ")))))

    def opcion3(self,viajero):
        print("Cantidad de millas actuales despues del Canje : {} ".format(viajero.canjearMillas(int(input(" Ingrese la cantidad de millas que quiere Canjear : ")))))

    def salida(self):
        print("Fin del Programa")
