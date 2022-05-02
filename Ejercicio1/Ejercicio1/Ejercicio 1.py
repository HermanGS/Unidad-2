import csv


class Email:

    def __init__(self,id,dominio,tipo,contrasenia):
        self.__id=id
        self.__dominio=dominio
        self.__tipo=tipo
        self.__contrasenia=contrasenia

    def retornaEmail(self):

        email = str(self.__id) + '@' + str(self.__dominio) + '.' + str(self.__tipoDominio)
        print('\nEstimado usuario: {}, te enviaremos tus mensajes a la direccion <{}>\n'.format(self.__id,email))
        return(email)

    def modifPassNWord(self):
        __a = 0
        while(__a==0):
            __contra = input("ingrese la vieja Contrasenia")
            if (__contra == self.__contrasenia):
                __n = input("ingrese la NUEVA contrasenia")
                self.__contrasenia=__n
            else:
                print("contrasenia incorrecta")

    def CrearCorreo(self,correo):
        cadena = correo.split('@')
        self.__id = cadena[0]
        cadena = cadena[1].split('.')
        self.__dominio = cadena[0]
        self.__tipoDominio = cadena[1]



if __name__ == '__main__':
    list = []
    archivo = open('datos.csv')
    reader = csv.reader(archivo)
    Id = input("ingrese la ID de la cuenta")
    Dominio = input("ingrese el dominio de la cuenta")
    tipo = input("ingrese el tipo de dominio de la cuenta")
    contrasenia = input("ingrese el password de la cuenta")
    e = Email(id,Dominio,tipo,contrasenia)
    print(e.retornaEmail())
    e.modifPassNWord()
    a = input("ingrese un correo")
    e.CrearCorreo(a)
    for fila in reader:
        cadena = str(fila).split('@')
        id = cadena[0]
        cadena = cadena[1].split('.')
        dominio = cadena[0]
        tipoDominio = cadena[1]
        email = Email(id,dominio,tipoDominio,0)
        list.append(email)
    for linea in list:
        print(linea)
