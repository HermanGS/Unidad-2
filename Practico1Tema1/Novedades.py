

from pickletools import read_uint1


class Novedades:
    __legajo: int
    __importe : float
    __concepto: str
    __codigo: str

    def __init__(self,legajo,importe,concepto,codigo):
        self.__legajo = legajo
        self.__importe = importe
        self.__concepto = concepto
        self.__codigo = codigo

    def __str__(self):
        return "legajo : {}, importe : {}, concepto : {}, codigo :{}".format(self.__legajo,self.__importe,self.__concepto,self.__codigo)

    def Mostrardatos(self):
        return "{:7}  {:7}  {:7}".format(self.__codigo,self.__concepto,self.__importe)
    
    def getLegajo(self):
        return self.__legajo
    
    def getImporte(self):
        return self.__importe

    def getCodigo(self):
        return self.__codigo

    