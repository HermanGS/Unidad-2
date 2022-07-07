

import re


class Personal:
    __legajo : int
    __dni: int
    __apellido : str
    __nombre : str
    __sueldo_basico = float

    def __init__(self,legajo,dni,apellido,nombre,sueldo_basico):
        self.__legajo = legajo
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo_basico = sueldo_basico


    def __str__(self):
        return "legajo : {}, dni : {}, apellido : {}, nombre : {}, sueldo básico : {}".format(self.__legajo,self.__dni,self.__apellido,self.__nombre,self.__sueldo_basico)


    def Mostrardatos(self):
        return "Apellido : {}   Nombre: {}\n DNI:{}".format(self.__apellido,self.__nombre,self.__dni)

    def getLegajo(self):
        return self.__legajo

    def getSueldo(self):
        return self.__sueldo_basico

    def getNombre(self):
        return self.__nombre

    def __gt__(self,other):
        resul = False
        if type(self) == type(other):
            if self.getNombre() > other.getNombre():
                resul = True
        return resul

    def __lt__(self,other):
        resul = False
        if type(self) == type(other):
            if self.getSueldo() < other.getSueldo():
                resul = True
        return resul