

class infracciones:

    def __init__(self,dni,patente,tipo_vehiculo,marca,fecha,descripcion,importe,estado):
        self.__dni = dni
        self.__patente = patente
        self.__tipo_vehiculo = tipo_vehiculo
        self.__marca = marca
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__importe = importe
        self.__estado = estado

    def __str__(self):
        return "dni {} patente {} tipo vehiculo {} marca {} fecha {} descripcion {} importe {} estado {}".format(self.__dni,self.__patente,self.__tipo_vehiculo,self.__marca,self.__fecha,self.__descripcion,self.__importe,self.__estado)

    def mostrardatos(self):
        return "{:^6}{:^10}{:^5}{:^9}{:^6}".format(self.__patente,self.__tipo_vehiculo,self.__marca,self.__descripcion,self.__importe)

    def getDni(self):
        return self.__dni

    def getPatente(self):
        return self.__patente
    
    def getDescripcion(self):
        return self.__descripcion

    def getImporte(self):
        return self.__importe

    def __eq__(self, other):
        val = False
        if type(self) == type(other):
            if self.getDni() == other.getDni() and self.getPatente() == other.getPatente() and self.getDescripcion() == other.getDescripcion():
                val = True
        return val
