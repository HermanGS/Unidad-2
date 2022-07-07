

class infractor:


    def __init__(self,dni, nombre, apellido, direccion, numero_carnet, puntaje):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__numero_carnet = numero_carnet
        self.__puntaje = puntaje


    def __str__(self):
        return "dni : {}, nombre : {}, apellido : {}, direccion : {}, numero carnet : {}, puntaje : {}".format(self.__dni,self.__nombre,self.__apellido,self.__direccion,self.__numero_carnet,self.__puntaje)
    
    def mostrardatos(self):
        return "Apellido: {} Nombre: {} DNI: {} \nCarnet: {}Dirección: {}".format(self.__apellido,self.__nombre,self.__dni,self.__numero_carnet,self.__direccion)


    def getDni(self):
        return self.__dni

    def setPuntos(self):
        self.__puntaje = self.__puntaje - int(10)