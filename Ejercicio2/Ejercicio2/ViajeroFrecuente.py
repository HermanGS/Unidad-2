
class Viajerofrecuente:

    def __init__(self,num_v,dni,nombre,apellido,millas_acum=0):
        self.__num_v = num_v
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def __str__(self):
        return ("{},{},{},{},{}".format(self.__num_v,self.__dni,self.__nombre,self.__apellido,self.__millas_acum))

    def cantidadTotaldeMillas(self):
        return(self.__millas_acum)

    def acumularMillas(self,cant_millas):
        self.__millas_acum = self.__millas_acum + cant_millas
        return(self.__millas_acum)

    def canjearMillas(self,cant_millasCanje):
        if cant_millasCanje <= self.__millas_acum:
            self.__millas_acum = self.__millas_acum - cant_millasCanje
            # print("cantidad de millas actuales:",self.__millas_acum," \n")
            return (self.__millas_acum)
        else:
            print("ERROR - Operación no valida - Cantidad de millas ingresada mayor a la que se posee")
    def retornaNUM(self):
        return (self.__num_v)
