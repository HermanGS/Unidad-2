

class Registro:
    __temperatura=0
    __humedad=0
    __presion=0

    def __init__(self,temperatura=0.0,humedad=0,presion=0.0):
        if(type(temperatura)==float)and(type(humedad)==int)and(type(presion)==float):
            self.__temperatura=temperatura
            self.__humedad=humedad
            self.__presion=float(presion)

    def getTemperatura(self):
        return (self.__temperatura)
    def getHumedad(self):
        return (self.__humedad)
    def getpresion(self):
        return (self.__presion)

    def __str__(self):
        return ("{:11}  {:6}  {:6}".format(self.__temperatura,self.__humedad,self.__presion))

