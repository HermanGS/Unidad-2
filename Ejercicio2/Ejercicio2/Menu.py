from ViajeroFrecuente import Viajerofrecuente
from ViajeroFrecuente import Viajerofrecuente

class Menu:
    # __opciones = {}
    # def opciones(self):
    #     self.__opciones = {
    #         1: self.opcion1,
    #         2: self.opcion2,
    #         3: self.opcion3,
    #         4: self.salida
    #     }
    pass

    def opcion1(self,viajero):
        print("Cantidad Total de millas : {} \n".format(viajero.cantidadTotaldeMillas()))
    def opcion2(self,viajero):
        print("Cantidad de millas Actuales despues de la Suma : {} \n".format(viajero.acumularMillas(int(input("Ingrese la cantidad de millas que ha recorrido para acumular : ")))))

    def opcion3(self,viajero):
        print("Cantidad de millas actuales despues del Canje : {} \n ".format(viajero.canjearMillas(int(input(" Ingrese la cantidad de millas que quiere Canjear : ")))))

    def salida(self):
        print("Fin del Programa")

    def opcion(self,op,viajero):
        if (op == 1):
            self.opcion1(viajero)
        if (op == 2):
            self.opcion2(viajero)
        if (op == 3):
            self.opcion3(viajero)
        if (op == 4):
            self.salida()







    # lambda: print("Opción Incorrecta"
'''
    def opcion(self,op,viajero):
        # f = self.__opciones.get(op, lambda: print ("Opcion Incorrecta"))
        # str(print(f))
        if (op=='1'or op=='2' or op== '3'):
            print("Entro al not none")
            self.__opciones[op](viajero)
        else:
            print("entro al none")
            self.__opciones[op]()
'''
